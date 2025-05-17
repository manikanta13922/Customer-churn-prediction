import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    database='churn_db',
    user='root',
    password='Mani@13922'  # Replace with your password
)
df = pd.read_sql('SELECT * FROM customers', connection)
connection.close()

# Clean TotalCharges
df['TotalCharges'] = df['TotalCharges'].replace(0, df['TotalCharges'].mean())

# Encode categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns
categorical_cols = categorical_cols.drop('customerID')
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Save preprocessed data
df.to_csv('data/preprocessed_churn.csv', index=False)
print("Preprocessing complete! Saved to preprocessed_churn.csv")