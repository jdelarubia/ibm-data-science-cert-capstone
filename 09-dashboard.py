## Import required libraries

from pathlib import Path

import dash
import pandas as pd
import plotly.express as px
import plotly.io as pio
from dash import Input, Output, dcc, html

import helpers as hlp

## Setup
pio.templates.default = "simple_white"

INPUT_FILE = hlp.DATA_DIR / Path("spacex_launch_dash.csv")

# Read spacex data into a pandas dataframe
spacex_df = pd.read_csv(INPUT_FILE)

# Get minimum and maximum payloads
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()
# Create a list of launch sites and add "all" as one of the options
sites_options = ["all"] + list(spacex_df["Launch Site"].unique())


app = dash.Dash(__name__)

# Create app layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        dcc.Dropdown(
            id="site-dropdown",
            options=sites_options,
            value="all",
            searchable=True,
        ),
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=min_payload,
            max=max_payload,
            step=1000,
            value=[min_payload, max_payload],
        ),
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


@app.callback(
    Output("success-pie-chart", component_property="figure"),
    [Input("site-dropdown", component_property="value")],
)
def generate_pie_chart(launch_site: str):
    if launch_site.lower() == "all":
        filtered_df = spacex_df[spacex_df["class"] == 1]

        # count the number of successful launches per site
        success_count = (
            filtered_df.groupby("Launch Site").size().reset_index(name="counts")
        )

        # Generates pie chart showing total success launches per site
        fig = px.pie(
            success_count,
            values="counts",
            names="Launch Site",
            title="Total Successful Launches by Site",
        )
    else:
        # filter the dataframe for the selected launch site
        filtered_df = spacex_df[
            spacex_df["Launch Site"].str.lower() == launch_site.lower()
        ]

        # Generates pie chart showing success (class=1) and failure (class=0) counts
        fig = px.pie(
            filtered_df,
            names="class",
            title=f"Total Success Launches from {launch_site}",
        )
    return fig


@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def generate_payload_chart(
    launch_site: str, payload_range: list[int] = [min_payload, max_payload]
):
    # get range and return graph
    low_bound, high_bound = payload_range
    if launch_site == "all":
        filtered_df = spacex_df[
            (spacex_df["Payload Mass (kg)"] >= low_bound)
            & (spacex_df["Payload Mass (kg)"] <= high_bound)
        ]
        title = f"Payload ({low_bound}-{high_bound} Kg) vs. Outcome for All Sites"
    else:
        filtered_df = spacex_df[
            spacex_df["Launch Site"].str.lower() == launch_site.lower()
        ]
        title = (
            f"Payload ({low_bound}-{high_bound} Kg) vs. Outcome for Site {launch_site}"
        )
    return px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title=title,
        labels={"class": "Launch Outcome (1=Success, 0=Failure)"},
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
