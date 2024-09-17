import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
traffic_data = pd.read_csv('chandigarh_traffic_data_september_2024_detailed.csv')

# Convert time column to datetime
traffic_data['time'] = pd.to_datetime(traffic_data['time'])

# Apply a rolling average to smooth the data
traffic_data['vehicle_count_smoothed'] = traffic_data.groupby('location')['vehicle_count'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())

# Set plot style
sns.set(style='whitegrid')

# Plot smoothed traffic patterns
plt.figure(figsize=(14, 7))
sns.lineplot(data=traffic_data, x='time', y='vehicle_count_smoothed', hue='location', linewidth=2.5)

# Enhance readability
plt.title('Smoothed Traffic Flow Patterns Over Time', fontsize=16)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Vehicle Count (Smoothed)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Location', fontsize=10)
plt.tight_layout()

# Add gridlines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()