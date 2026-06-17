# Oasis: Unemployment Prediction Dashboard

## Project Overview

This project analyzes unemployment data in India and builds machine learning models to predict unemployment rates based on regional and demographic factors. It also provides an interactive Streamlit dashboard for data visualization and unemployment rate prediction.

---

## Features

* Cleaned and merged unemployment datasets
* Trained Linear Regression and Random Forest models
* Fine-tuned Random Forest for improved performance
* Saved trained models using Joblib for future use
* Interactive Streamlit dashboard for:

  * Predicting unemployment rates by region and area
  * Visualizing unemployment trends over time
  * Comparing Rural vs Urban unemployment
  * Comparing predicted and actual unemployment rates

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## Project Structure

```text
oasis/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── models/
│   └── random_forest_model.pkl
│
├── notebooks/
│   └── 1_data_cleaning.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Model Development

### Linear Regression

* Used as a baseline model for unemployment prediction.

### Random Forest Regressor

* Trained and fine-tuned for improved prediction accuracy.
* Saved using Joblib for deployment in the Streamlit application.

---

## Results

* Successfully analyzed unemployment trends across different regions.
* Developed machine learning models for unemployment rate prediction.
* Built an interactive Streamlit dashboard for visualization and forecasting.
* Random Forest model provided better prediction performance than the baseline model.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/swethasuresh1905/oasis.git
cd oasis
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

---

## Dependencies

* Python 3.8+
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## Future Enhancements

* Add additional forecasting models
* Deploy dashboard to cloud platforms
* Add real-time unemployment data updates
* Improve dashboard visualizations

---

## Author

**Swetha Suresh**

B.Tech Artificial Intelligence & Data Science
