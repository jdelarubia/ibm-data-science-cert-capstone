# Applied Data Science Capstone

In this module, you will compile all of your activities into one place and deliver your data-driven insights to determine if the first stage of Falcon 9 will land successfully.

---

## TOC

- [Applied Data Science Capstone](#applied-data-science-capstone)
  - [TOC](#toc)
  - [Learning Objectives](#learning-objectives)
  - [Project init](#project-init)
  - [Project Support Notebooks \& code](#project-support-notebooks--code)
  - [Conclusions](#conclusions)

---

## Learning Objectives

- Establish how to structure and build your data-findings report.
- Submit your final report for peer review.
- Review the work submitted by your peers.

---

## Project init

```bash
uv init
uv add ipykernel pandas numpy requests beautifulsoup4 matplotlib seaborn folium scikit-learn dash plotly prettytable ipython-sql

# or,

python3 -m venv .venv
python3 -m pip install ipykernel pandas numpy requests beautifulsoup4 matplotlib seaborn folium scikit-learn dash plotly prettytable ipython-sql
```

---

## Project Support Notebooks & code

1. [Data collection](./01-data-collection.ipynb)
2. [Data Wrangling](./02-data-wrangling.ipynb)
3. [Data Scraping from Wikipedia](./03-data-scraping.ipynb)
4. [EDA: Basic Analysis](./04-eda-basic.ipynb)
5. [EDA: SQL](./05-eda-sql.ipynb)
6. [EDA: Falcon 9 First Stage Landing Prediction](./06-eda-predictions.ipynb)
7. [EDA: Folium](./07-eda-folium.ipynb)
8. [ML: Predictive analysis](./08-predictions.ipynb)
9. [Dash: analysis](./09-dash-analysis.ipynb)
   1. [Dash server code](./09-dashboard.py)
      run `python 09-dashboard.py` and visit `http://127.0.0.1:8050` from your browser to see the dashboard.

---

## Conclusions

- Number of successful launches increases has increased over the last years, significantly from 2015. The success trend seems to stabilize at a 60 - 90% ratio from 2016 onwards.
- The number of launches has also increased, so the successes have gone up. VAFB show the best ratio of succeeded launches. KSC doesn’t show information below almost 40 launches.
- Orbits such as ES-L1, GEO, HEO and SSO show a 100% success launch rate. On the contrary, GTO reaches only a ~50% success rate.
- Launch sites KSC LC-39A has a higher success launch rate (~77%) while CCAFS LC40 has the worst ratio with a ~73% of failures.
- Launch sites are located relatively far from cities, while they do locate close to the shore and facilities as railroads.
- Payloads between 2000 and 5000 kg have a higher success rate (~62%). On the other hand, the ranges 0 - 2000 kg (77%), 5000 - 7000 kg (78%) show the highest failure rates.
- Falcon 9 FT boosters have a ~67% success rate.
- In our train/test split data examples, Logistic Regression perform best on training data (~86%), while SVM and LR (83% on both cases) do on test data.

---
