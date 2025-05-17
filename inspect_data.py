import pandas as pd

     # Load dataset
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())  # View first 5 rows
print(df.info())  # Check data types and missing values
print(df.isnull().sum())  # Check for missing values
