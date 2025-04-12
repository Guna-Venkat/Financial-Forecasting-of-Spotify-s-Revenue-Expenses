# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ---------- Load Your Data ----------
# Replace this with your actual data loading
df = pd.read_csv("formatted_original_data.csv")  # e.g., with 'date', 'total_revenue', ...
forecast_df = pd.read_csv("forecast_output.csv")  # e.g., with 'date', 'total_revenue', ...

# Convert date columns
df['date'] = pd.to_datetime(df['date'])
forecast_df['date'] = pd.to_datetime(forecast_df['date'])

# ---------- Streamlit Setup ----------
st.set_page_config(page_title="📊 Business Forecast Dashboard", layout="wide")
st.title("📈 Business Forecast Dashboard")
st.markdown("Visualizing key business metrics with actionable insights for the next 4 quarters.")

# ---------- Plot Section ----------
st.header("📊 Forecasted Metrics vs Historical Trends")

keys_to_plot = ['total_revenue', 'premium_revenue', 'maus', 'premium_maus', 'premium_arpu', 'r_and_d_cost']
n_rows = 2
n_cols = 3

fig, axs = plt.subplots(n_rows, n_cols, figsize=(18, 10))
fig.tight_layout(pad=4.0)
fig.subplots_adjust(top=0.9)
fig.suptitle("Forecasted Business Metrics vs Historical", fontsize=16)

for i, key in enumerate(keys_to_plot):
    row, col = divmod(i, n_cols)
    axs[row, col].plot(df['date'], df[key], label="Historical", color='steelblue', linewidth=2)
    axs[row, col].plot(forecast_df['date'], forecast_df[key], label="Forecast", color='orange', linestyle='--', marker='o', linewidth=2)
    axs[row, col].set_title(key.replace('_', ' ').title(), fontsize=12)
    axs[row, col].tick_params(axis='x', rotation=45)
    axs[row, col].legend()

st.pyplot(fig)

# ---------- Actions Section ----------
st.header("✅ Action Plan Based on Forecasts")

forecast_actions = {
    "total_revenue": "As forecast for `total_revenue` is increasing, scale marketing and strengthen customer support and logistics to meet demand.",
    "premium_revenue": "As forecast for `premium_revenue` is increasing, invest in premium feature promotion and exclusive content to attract more paid users.",
    "maus": "As forecast for `maus` is increasing, ensure seamless onboarding and roll out gamified user engagement features.",
    "premium_maus": "As forecast for `premium_maus` is increasing, launch referral programs and upgrade nudges to boost free-to-paid conversions.",
    "premium_arpu": "As forecast for `premium_arpu` is flat, introduce tiered pricing, bundled offerings, or exclusive add-ons.",
    "r_and_d_cost": "As forecast for `r_and_d_cost` is steady, allocate resources to high-impact innovation and monitor ROI from R&D initiatives."
}

for key in keys_to_plot:
    st.subheader(f"📌 {key.replace('_', ' ').title()}")
    st.markdown(forecast_actions[key])
