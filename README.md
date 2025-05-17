# Customer Churn Prediction Dashboard

## Overview
This project builds a dashboard to predict and visualize customer churn using a telecom dataset. It involves data preprocessing, machine learning, and visualization.

## Prerequisites
- Python 3.x
- MySQL
- Power BI Desktop
- Libraries: pandas, scikit-learn, joblib, mysql-connector-python

## Project Structure
- data/: Contains raw and preprocessed data (raw_data.csv, preprocessed_churn.csv, powerbi_data.csv).
- models/: Contains the trained model (rf_model.pkl).
- preprocess.py: Script for data preprocessing.
- train_model.py: Script for model training.
- generate_predictions.py: Script to generate predictions for Power BI.
- churn_dashboard.pbix: Power BI dashboard file.

## Steps
1. *Load Data into MySQL*: Import raw_data.csv into a MySQL database.
2. *Preprocess Data*: Run preprocess.py to clean and preprocess the data.
3. *Exploratory Data Analysis (EDA)*: Analyze the dataset (done manually or via code).
4. *Train Model*: Run train_model.py to train a Random Forest model.
5. *Create Power BI Dashboard*:
   - Run generate_predictions.py to generate predictions.
   - Build a dashboard in Power BI with four visualizations.
6. *Test Real-Time Data*: Add a test customer in MySQL, rerun scripts, and refresh the dashboard.
7. *Document*: Create this README.

## Visualizations
- *Churn Distribution*: Bar chart showing actual churn counts.
- *Predicted Churn Distribution*: Bar chart showing predicted churn counts.
- *Average Tenure by Churn*: Bar chart comparing average tenure for churned vs. non-churned customers.
- *Monthly Charges by Churn*: Line chart showing monthly charges distribution by churn status.

## Usage
- Open churn_dashboard.pbix in Power BI Desktop.
- Refresh the dashboard to update with new data.
- Interact with the visuals (e.g., click a bar to filter other charts).