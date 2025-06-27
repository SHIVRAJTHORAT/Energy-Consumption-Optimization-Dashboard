# energy_dashboard.py

# 1. Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Optional: For better visuals in plots
sns.set(style='whitegrid')

# 2. Simulate sample energy consumption data
# Replace this section with your actual CSV file in production
np.random.seed(42)  # for reproducibility
data = {
    'Timestamp': pd.date_range(start='2025-01-01', periods=1000, freq='H'),
    'Location': np.random.choice(['Pune', 'Mumbai', 'Delhi'], size=1000),
    'Appliance': np.random.choice(['AC', 'Heater', 'Refrigerator', 'Washing Machine', 'TV'], size=1000),
    'Consumption_kWh': np.round(np.random.uniform(0.1, 5.0, size=1000), 2),
    'Temperature': np.round(np.random.uniform(18, 42, size=1000), 1),
    'Weather': np.random.choice(['Sunny', 'Cloudy', 'Rainy'], size=1000)
}
df = pd.DataFrame(data)

# 3. Data preprocessing and feature extraction
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.day_name()
df['Month'] = df['Timestamp'].dt.month_name()
df['Date'] = df['Timestamp'].dt.date

# 4. Aggregated analytics

# Total daily consumption
daily_usage = df.groupby('Date')['Consumption_kWh'].sum().reset_index()

# Appliance-wise consumption
appliance_usage = df.groupby('Appliance')['Consumption_kWh'].sum().reset_index()

# Average hourly usage across days
hourly_usage = df.groupby('Hour')['Consumption_kWh'].mean().reset_index()

# Top 5 high-consumption records (for recommendations)
top_usage = df.sort_values(by='Consumption_kWh', ascending=False).head(5)

# 5. Optional: Save the processed data for Power BI use
df.to_csv("processed_energy_data.csv", index=False)
daily_usage.to_csv("daily_usage.csv", index=False)
appliance_usage.to_csv("appliance_usage.csv", index=False)
hourly_usage.to_csv("hourly_usage.csv", index=False)

# 6. Visualizations
# Line plot - Daily energy usage
plt.figure(figsize=(12, 5))
sns.lineplot(data=daily_usage, x='Date', y='Consumption_kWh', color='green')
plt.title("Daily Energy Consumption")
plt.xlabel("Date")
plt.ylabel("Total Consumption (kWh)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot - Appliance-wise energy usage
plt.figure(figsize=(10, 5))
sns.barplot(data=appliance_usage.sort_values('Consumption_kWh', ascending=False),
            x='Appliance', y='Consumption_kWh', palette='magma')
plt.title("Total Energy Consumption by Appliance")
plt.xlabel("Appliance")
plt.ylabel("Consumption (kWh)")
plt.tight_layout()
plt.show()

# Line plot - Hourly average usage
plt.figure(figsize=(10, 5))
sns.lineplot(data=hourly_usage, x='Hour', y='Consumption_kWh', marker='o', color='blue')
plt.title("Average Hourly Energy Consumption")
plt.xlabel("Hour of Day")
plt.ylabel("Average Consumption (kWh)")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# 7. Simple Recommendations based on top usage
print("\n🔍 Top 5 Highest Energy Usage Records:")
print(top_usage[['Timestamp', 'Location', 'Appliance', 'Consumption_kWh', 'Temperature', 'Weather']])

# Optional: Flag high usage records
df['Usage_Flag'] = df['Consumption_kWh'].apply(
    lambda x: 'High' if x > 4 else 'Moderate' if x > 2 else 'Optimal'
)

# Save this flagged data for Power BI
df.to_csv("energy_data_flagged.csv", index=False)

print("\n✅ Data processed and saved. Visualizations completed.")
