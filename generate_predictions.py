import pandas as pd
import joblib

# Load data and model
df = pd.read_csv('data/preprocessed_churn.csv')
model = joblib.load('models/rf_model.pkl')

# Predict churn
X = df.drop(['customerID', 'Churn'], axis=1)
df['PredictedChurn'] = model.predict(X)

# Save for Power BI
df.to_csv('data/powerbi_data.csv', index=False)
print("Power BI data saved to powerbi_data.csv")