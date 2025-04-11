# ⚙️ Project Setup Guide: Spotify Financial Forecasting

This guide helps you set up a complete development environment for the **Spotify Financial Forecasting** project using Anaconda and Python.

---

## 🧰 Step 1: Install Anaconda (If Not Installed)

🔗 [Download Anaconda](https://www.anaconda.com/products/distribution)

- Choose the latest **Python 3.10** version for your operating system.
- Follow the installer instructions.
- After installation, open **Anaconda Prompt** (Windows) or Terminal (macOS/Linux).

---

## 🛠️ Step 2: Clone the Project Repository

If hosted on GitHub:

git clone https://github.com/Guna-Venkat/Financial-Forecasting-of-Spotify-s-Revenue-Expenses.git

Or create your own:

mkdir spotify-forecasting
cd spotify-forecasting
mkdir data notebooks app models
touch README.md setup.md requirements.txt .gitignore

## 📦 Step 3: Create and Activate Conda Environment
conda create --name spotify-forecast python=3.10 -y
conda activate spotify-forecast

## 📜 Step 4: Install Project Dependencies
Use the requirements.txt file to install all packages.
Then run:
pip install -r requirements.txt
⚠️ Note: prophet might take a while and may require build tools. If you face issues, try:
pip install --upgrade pip
pip install prophet --no-binary :all:

## 🚀 Step 6: Run Jupyter Notebook
jupyter notebook notebooks/EDA_and_forecasting.ipynb
## 🌐 Step 7: Run the Web App
If using Streamlit:
streamlit run app/app.py
If using Gradio:
python app/app.py
## ✅ Step 8: (Optional) Export Conda Environment
To export the full environment:
conda env export > environment.yml
To recreate it on another system:
conda env create -f environment.yml
conda activate spotify-forecast
## 🧹 Step 9: Add .gitignore
Here's a basic .gitignore file:
__pycache__/
.ipynb_checkpoints/
.env
*.pkl
.DS_Store
.env
.vscode/
*.pyc
