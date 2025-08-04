# Applied Data Science Capstone

In this module, you will compile all of your activities into one place and deliver your data-driven insights to determine if the first stage of Falcon 9 will land successfully.

## Learning Objectives

- Establish how to structure and build your data-findings report.
- Submit your final report for peer review.
- Review the work submitted by your peers.

---

## TOC

- [Applied Data Science Capstone](#applied-data-science-capstone)
  - [Learning Objectives](#learning-objectives)
  - [TOC](#toc)
  - [Project init](#project-init)
  - [Support Notebooks](#support-notebooks)

---

## Project init

```bash
uv init
uv add ipykernel pandas numpy requests beautifulsoup4 matplotlib seaborn folium scikit-learn dash plotly

# or,

python3 -m venv .venv
python3 -m pip install ipykernel pandas numpy requests beautifulsoup4 matplotlib seaborn folium scikit-learn dash plotly
```

---

## Support Notebooks

1. [Data collection](./01-data-collection.ipynb)
2. [Data Wrangling](./02-data-wrangling.ipynb)
3. [Data Scraping from Wikipedia](./03-data-scraping.ipynb)
4. [EDA: Basic Analysis](./04-eda-basic.ipynb)
5. [EDA: SQL](./05-eda-sql.ipynb)
6. [EDA: Falcon 9 First Stage Landing Prediction](./06-eda-predictions.ipynb)
7. [EDA: Folium](./07-eda-folium.ipynb)
8. [Predictions](./08-predictions.ipynb)
9. [Dash: analysis](./09-dash-analysis.ipynb)
   1. [Dash server code](./09-dashboard.py)

---
