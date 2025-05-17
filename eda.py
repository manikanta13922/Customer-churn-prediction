import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed data
df = pd.read_csv('data/preprocessed_churn.csv')

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['int64', 'float64', 'int32', 'float32'])

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('plots/correlation_heatmap.png')
plt.close()

# Churn distribution
sns.countplot(x='Churn', data=df)
plt.title('Churn Distribution')
plt.savefig('plots/churn_distribution.png')
plt.close()

# Tenure vs Churn
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title('Tenure vs Churn')
plt.savefig('plots/tenure_vs_churn.png')
plt.close()

print("EDA plots saved in 'plots' folder!")