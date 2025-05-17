import pandas as pd
import mysql.connector
from mysql.connector import Error

# Load dataset
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Clean TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='churn_db',
        user='root',
        password='Mani@13922'  # Replace with your MySQL password
    )
    cursor = connection.cursor()

    # Insert data
    insert_query = """
    INSERT INTO customers (customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
    PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection,
    TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
    MonthlyCharges, TotalCharges, Churn)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for row in df.itertuples():
        values = (
            row.customerID, row.gender, row.SeniorCitizen, row.Partner, row.Dependents,
            row.tenure, row.PhoneService, row.MultipleLines, row.InternetService,
            row.OnlineSecurity, row.OnlineBackup, row.DeviceProtection, row.TechSupport,
            row.StreamingTV, row.StreamingMovies, row.Contract, row.PaperlessBilling,
            row.PaymentMethod, row.MonthlyCharges, row.TotalCharges, row.Churn
        )
        cursor.execute(insert_query, values)

    connection.commit()
    print("Data loaded successfully!")

except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()