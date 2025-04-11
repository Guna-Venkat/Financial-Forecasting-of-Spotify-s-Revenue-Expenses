# 📈 Financial Forecasting of Spotify's Revenue & Expenses

### Forecasting Spotify’s Financial Health: Time Series Modeling of Revenue & Expense Trends

---

## 🧠 1. Problem Statement

Spotify, as a fast-growing audio streaming company, operates on thin margins and rapidly changing user behavior. Accurate forecasting of **revenue**, **expenses**, and **premium user growth** is crucial for financial planning, marketing strategy, and investor decision-making.

**Your goal is to:**

> Analyze and forecast Spotify’s **monthly revenues**, **expenses**, and **premium user counts** using time series techniques, and develop an **interactive dashboard** to visualize trends and predictions.

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
