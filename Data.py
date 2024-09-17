import pandas as pd
import numpy as np

# Set the date range for September 2024 with 30-minute intervals
date_range = pd.date_range(start='2024-09-01', end='2024-09-30', freq='h')

# Define locations within Chandigarh
locations = ['Sector 17', 'Sector 22', 'IT Park']

# Estimate vehicle counts based on assumed traffic density
vehicle_count_estimates = {
    'Sector 17': (150, 300),
    'Sector 22': (100, 200),
    'IT Park': (80, 180)
}

# Generate synthetic data
np.random.seed(42)  # For reproducibility
data = []

for location in locations:
    low, high = vehicle_count_estimates[location]
    vehicle_counts = np.random.randint(low, high, size=len(date_range))
    for time, count in zip(date_range, vehicle_counts):
        data.append({'time': time, 'location': location, 'vehicle_count': count})

# Create DataFrame
traffic_data = pd.DataFrame(data)

# Display the first few rows
print(traffic_data.head())

# Save to CSV
traffic_data.to_csv('chandigarh_traffic_data_september_2024_detailed.csv', index=False)