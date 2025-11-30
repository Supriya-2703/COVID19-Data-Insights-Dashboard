import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------
# MUST BE FIRST STREAMLIT COMMAND
# -------------------------------------------------------
st.set_page_config(page_title="COVID-19 Data Insights Dashboard", layout="wide")

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv")   # Your dataset file
    return df

df = load_data()

# -------------------------------------------------------
# Page Title
# -------------------------------------------------------
st.title("🦠 COVID-19 Data Insights Dashboard")
st.write("Analyze worldwide COVID-19 cases, deaths, vaccinations, and trends.")

# -------------------------------------------------------
# Sidebar – Country Selection
# -------------------------------------------------------
countries = sorted(df["location"].unique())
selected_country = st.sidebar.selectbox("🌍 Select Country", countries)

# Filter data for selected country
country_df = df[df["location"] == selected_country]

# -------------------------------------------------------
# Key Metrics
# -------------------------------------------------------
st.subheader(f"📊 Key Statistics for {selected_country}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Cases",
        f"{country_df['total_cases'].max():,.0f}"
        if "total_cases" in country_df.columns else "N/A"
    )

with col2:
    st.metric(
        "Total Deaths",
        f"{country_df['total_deaths'].max():,.0f}"
        if "total_deaths" in country_df.columns else "N/A"
    )

with col3:
    if "total_vaccinations" in country_df.columns and country_df["total_vaccinations"].notna().sum() > 0:
        st.metric("Total Vaccinations", f"{country_df['total_vaccinations'].max():,.0f}")
    else:
        st.metric("Total Vaccinations", "Data Not Available")

with col4:
    st.metric(
        "Population",
        f"{country_df['population'].max():,.0f}"
        if "population" in country_df.columns else "N/A"
    )

# -------------------------------------------------------
# Total Cases Over Time
# -------------------------------------------------------
st.subheader("📈 Total Cases Over Time")

if "total_cases" in country_df.columns:
    fig_cases = px.line(
        country_df,
        x="date",
        y="total_cases",
        title=f"Total COVID-19 Cases in {selected_country}"
    )
    st.plotly_chart(fig_cases, use_container_width=True)
else:
    st.warning("No total case data available.")

# -------------------------------------------------------
# Total Deaths Over Time
# -------------------------------------------------------
st.subheader("⚰️ Total Deaths Over Time")

if "total_deaths" in country_df.columns:
    fig_deaths = px.line(
        country_df,
        x="date",
        y="total_deaths",
        title=f"Total COVID-19 Deaths in {selected_country}"
    )
    st.plotly_chart(fig_deaths, use_container_width=True)
else:
    st.warning("No death data available.")

# -------------------------------------------------------
# Vaccination Progress
# -------------------------------------------------------
st.subheader("💉 Vaccination Progress Over Time")

if "total_vaccinations" in country_df.columns and country_df["total_vaccinations"].notna().sum() > 0:
    fig_vacc = px.line(
        country_df,
        x="date",
        y="total_vaccinations",
        title=f"Vaccination Progress in {selected_country}"
    )
    st.plotly_chart(fig_vacc, use_container_width=True)
else:
    st.info(f"Vaccination data not available for {selected_country}.")

# -------------------------------------------------------
# Daily New Cases
# -------------------------------------------------------
st.subheader("📉 Daily New Cases")

if "new_cases" in country_df.columns:
    fig_daily = px.bar(
        country_df,
        x="date",
        y="new_cases",
        title=f"Daily New Cases in {selected_country}"
    )
    st.plotly_chart(fig_daily, use_container_width=True)
else:
    st.warning("No daily new cases data available.")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown("---")
st.markdown("**Developed by Supriya Shahaji Bhade**")
