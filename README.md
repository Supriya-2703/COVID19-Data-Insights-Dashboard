# 🦠 COVID-19 Data Insights Dashboard — EDA

This project performs a comprehensive Exploratory Data Analysis (EDA) on global COVID-19 data to uncover trends in confirmed cases, deaths, recoveries, testing, and vaccinations.
It also includes an interactive Streamlit dashboard that helps visualize country-wise and worldwide patterns across time.

![Streamlit UI](https://img.shields.io/badge/Made%20With-Streamlit-red?logo=streamlit)

<img width="1120" height="832" alt="Image" src="https://github.com/user-attachments/assets/94b207fd-977c-4964-a69b-d4e21039da85" />

# 📌 Features of the Project

## 🔍 1. Data Cleaning & Preprocessing

- Handling missing values
- Converting date formats
- Selecting relevant COVID-19 metrics
- Creating derived metrics (e.g., active cases, CFR)
- Exporting cleaned dataset (covid_cleaned.csv)

## 📊 2. Exploratory Data Analysis (EDA)

- Includes visual analysis of:
- Daily & cumulative COVID-19 cases
- Death trends and fatality ratios
- Vaccination progress
- Country-wise comparisons
- Time-series line charts
- Heatmaps & distribution plots

## 🧠 3. Insights

- Countries with early vaccination rollout show a noticeable decline in new cases
- Case fatality rate varies significantly across regions
- Variant waves create distinct peaks in global trend lines
- Testing rates correlate with confirmed case spikes
- Population density influences spread intensity

## 🖥 4. Interactive Streamlit Dashboard

The dashboard offers:
- Country-wise case comparison
- Global overview metrics
- Trend analysis line charts
- Vaccination progress visualization
- Sidebar filters for:
- Countries
- Metrics (Cases, Deaths, Recovered, Vaccinations)
- Date ranges

1.Run the dashboard:
streamlit run app.py

## 📁 Project Structure
📦 COVID19-Data-Insights-Dashboard

├── Notebook.ipynb

├── Image.png

├── app.py

├── owid-covid-data.csv

└── README.md

## 🚀 How to Run the Project
1️⃣ Install Dependencies:

pip install -r requirements.txt
Or install manually:
pip install pandas numpy matplotlib streamlit plotly

2️⃣ Run EDA in Jupyter Notebook:

Open eda_notebook.ipynb and run all cells.

3️⃣ Launch Dashboard:

streamlit run app.py

## 🌟 Project Summary

This project provides a complete exploration of COVID-19 global trends using clear visualizations and interactive analytics.
It showcases how confirmed cases, deaths, vaccinations, and testing evolved over time, helping understand pandemic dynamics through real-world data.
The Streamlit dashboard makes these insights easily accessible with visual, interactive charts.

## 📌 Future Enhancements

- Add prediction model (ARIMA / Prophet) for future case forecasting
- Add vaccination dose-level details
- Add interactive maps (Geo visualizations)
- Deploy dashboard on Streamlit Cloud / HuggingFace
- Add automated daily dataset updates

## 📃 License

This project is licensed under the MIT License – see the LICENSE file for details.
