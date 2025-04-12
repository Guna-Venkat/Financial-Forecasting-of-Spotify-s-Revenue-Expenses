# 📈 Financial Forecasting of Spotify's Revenue & Expenses

### Forecasting Spotify’s Financial Health: Time Series Modeling of Revenue & Expense Trends

---

## 🧠 1. Problem Statement

Spotify, as a fast-growing audio streaming company, operates on thin margins and rapidly changing user behavior. Accurate forecasting of **revenue**, **expenses**, and **premium user growth** is crucial for financial planning, marketing strategy, and investor decision-making.

**Your goal is to:**

> Analyze and forecast Spotify’s **monthly revenues**, **expenses**, and **premium user counts** using time series techniques, and develop an **interactive dashboard** to visualize trends and predictions.

**Output:**
## 📊 Forecast Dashboard Preview

![Forecast Dashboard]([https://github.com/Guna-Venkat/Financial-Forecasting-of-Spotify-s-Revenue-Expenses/tree/main/assets](https://github.com/Guna-Venkat/Financial-Forecasting-of-Spotify-s-Revenue-Expenses/blob/main/assets/forecast_image.PNG))

---

## 🔍 2. Dataset

**Source**: [Kaggle - Spotify Revenue & Premium Users Dataset](https://www.kaggle.com/datasets/mauryansshivam/spotify-revenue-expenses-and-its-premium-users)

**Contains columns like:**

- `Month` (Date)
- `Revenue` (USD Million)
- `Expenses` (USD Million)
- `Premium Users` (Millions)

---

## 🛠️ 3. Tech Stack

| Category              | Tools/Tech Used                      |
|-----------------------|--------------------------------------|
| **Data Processing**   | `pandas`, `numpy`                    |
| **Visualization**     | `matplotlib`, `seaborn`, `plotly`   |
| **Forecasting Models**| `Prophet`, `ARIMA` (`statsmodels`)  |
| **Evaluation Metrics**| `RMSE`, `MAE`, `MAPE`                |
| **UI Dashboard**      | `Gradio` or `Streamlit`             |
| **Deployment**        | `Streamlit Cloud`, `Render`         |

---

## 📦 4. Project Structure

```bash
spotify-forecasting/
│
├── data/
│   └── spotify_financials.csv
│
├── notebooks/
│   └── EDA_and_forecasting.ipynb
│
├── app/
│   └── app.py  # Gradio or Streamlit app
│
├── models/
│   └── prophet_model.pkl
│
├── README.md
├── requirements.txt
└── .gitignore
```
## 🧾 Glossary of Key Financial Metrics

| **Term**                  | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| Total Revenue            | Combined income from all sources (premium + ads).                               |
| Premium Revenue          | Income from Spotify subscriptions.                                              |
| Ad Revenue               | Income from advertising (free-tier users).                                      |
| Cost of Revenue          | Total cost to deliver the service (e.g., royalties, streaming infra).           |
| Gross Profit             | Total Revenue - Cost of Revenue.                                                |
| Premium/Ad Cost Revenue  | Respective costs for premium/ad services.                                       |
| MAUs                     | Monthly Active Users (Total, Premium, Ad-supported).                            |
| Premium ARPU             | Average Revenue Per Premium User.                                               |
| R&D / S&M / G&A Costs    | Research, Sales & Marketing, and General/Admin expenses.                        |

---

## Key Insights from EDA (2017–2023)

### 💡 1. Revenue Growth is Premium-Driven
- **Premium Revenue** grew from **$828M (Q1 2017)** to **$2.7B (Q1 2023)** — more than a **3x increase**.
- **Ad Revenue** saw minor growth: from **$74M** to **$329M** in the same period.
- This confirms that **Spotify’s primary revenue engine is its subscription model**.

---

### 💡 2. Gross Profit Mirrors Premium Trends
- **Premium Gross Profit** increased in sync with Premium Revenue, highlighting **consistent margins**.
- **Ad Gross Profit** remains much lower and even negative at times (e.g., **Q1 2023: -$10M**), indicating **ad segment inefficiencies or high costs**.

---

### 💡 3. MAUs Have Grown, But Premium Users Lead
- **Total MAUs** rose from **131M (Q1 2017)** to **515M (Q1 2023)**.
- **Premium MAUs** nearly **quadrupled**, indicating:
  - Higher customer retention.
  - Successful conversion from free-tier to paid users.
- **Ad MAUs** increased too, but at a slower pace.

---

### 💡 4. ARPU Is Stable with a Slight Downtrend
- **Premium ARPU** declined from **$5.46 (Q1 2017)** to **$4.32 (Q1 2023)**.
- Suggests:
  - **Global expansion** into markets with lower pricing.
  - **Discount plans** or family/student bundles impacting ARPU.

---

### 💡 5. Costs Are Rising, But So Is Efficiency
- **Cost of Revenue** grew, but at a slower rate than revenue.
- **Sales & Marketing** and **R&D** costs increased, signaling:
  - Stronger brand push.
  - Continued product innovation.
- **Gross Profit** also improved, indicating better **operational efficiency**.

---

### 💡 6. Ad Business is Not Yet Profitable
- Ad Revenue often **barely covers Ad Cost**, and **Gross Profit is frequently low or negative**.
- Suggests Spotify might:
  - Be using ads mainly as a funnel to Premium.
  - Still be experimenting with the ad model's optimization.

---

### 📌 Final Observations
- Spotify is steadily evolving from an ad-supported platform to a **premium subscription-first model**.
- With steady MAU growth and stable ARPU, the business shows strong fundamentals.
- Strategic focus should be:
  - Improving **ad profitability**.
  - **Innovating pricing models** to improve ARPU without losing users.

