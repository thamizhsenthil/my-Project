# regional_demand_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
file_path = 'regional_demand.csv'  # Ensure this matches your exported file
if not os.path.exists(file_path):
    raise FileNotFoundError("Export your SQL results to 'regional_demand.csv' first.")

df = pd.read_csv(file_path, parse_dates=['order_month'])

# ===============================
# 1. Data Cleaning & Preparation
# ===============================
# Ensure data types are correct
df['customer_state'] = df['customer_state'].astype(str)
df = df.sort_values(by=['customer_state', 'order_month'])

# ===============================
# 2. Plot: Monthly Demand by Region
# ===============================
plt.figure(figsize=(14, 7))
for state in df['customer_state'].unique():
    state_df = df[df['customer_state'] == state]
    plt.plot(state_df['order_month'], state_df['total_orders'], label=state)

plt.title('Monthly Demand by Region (State)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Total Orders')
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()

# ===============================
# 3. Plot: Regional Sales Distribution (Total)
# ===============================
sales_by_state = df.groupby('customer_state')['total_sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=sales_by_state.index, y=sales_by_state.values, palette='viridis')
plt.title('Total Sales Distribution by Region', fontsize=16)
plt.xlabel('Customer State')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# ===============================
# 4. Save Cleaned Data (Optional)
# ===============================
df.to_csv('cleaned_regional_demand.csv', index=False)
print("Visualizations complete. Cleaned data saved as 'cleaned_regional_demand.csv'.")
