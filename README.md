# Oasis: Unemployment Prediction Dashboard

## Project Overview
This project analyzes unemployment data in India and builds a machine learning model to **predict unemployment rates** based on regional and demographic features. It also provides an **interactive Streamlit dashboard** for visualization and predictions.

---

## Features
- Cleaned and merged unemployment datasets  
- Trained **Linear Regression** and **Random Forest** models  
- Fine-tuned Random Forest for improved accuracy  
- Saved trained model for reuse using `joblib`  
- Interactive Streamlit dashboard for:
  - Predicting unemployment rates by region and area  
  - Visualizing trends over time  
  - Comparing Rural vs Urban unemployment  
  - Comparing predicted vs actual unemployment rates  

---

## Folder Structure
oasis/
│
├── data/
│ ├── raw/ # Original datasets
│ └── cleaned/ # Cleaned/merged datasets
│
├── models/ # Saved Random Forest model (.pkl)
│
├── notebooks/ # Jupyter notebooks
│ └── 1_data_cleaning.ipynb
│
├── app.py # Streamlit dashboard script
├── requirements.txt # Python dependencies
└── README.md



---

## How to Run the Dashboard
1. Clone this repository:
```bash
git clone https://github.com/swethasuresh1903/oasis.git
Navigate to the project folder:

##navigate to project folder
cd oasis

##create visual env
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell

##install dependencies
pip install -r requirements.txt


##to run streamlit app
streamlit run app.py


##Dependencies
Python 3.8+

pandas

numpy

scikit-learn

matplotlib

seaborn

streamlit

joblib

##nstall dependecies via 
pip install -r requirements.txt

Author
Swetha Suresh
Email: swethasuresh1905@gmail.com