import numpy as np

# Redefine np.float_ to np.float64
np.float_ = np.float64

import warnings
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Redefine np.float_ to np.float64 (if needed)
np.float_ = np.float64

# Load and prepare data
traffic_data = pd.read_csv('chandigarh_traffic_data_september_2024_detailed.csv')
traffic_data['time'] = pd.to_datetime(traffic_data['time'])

# Filter data for one location (e.g., Sector 17)
location_data = traffic_data[traffic_data['location'] == 'Sector 17']
df = location_data[['time', 'vehicle_count']].rename(columns={'time': 'ds', 'vehicle_count': 'y'})

# Initialize and fit the model
model = Prophet()
model.fit(df)

# Create a dataframe for future dates
future = model.make_future_dataframe(periods=48, freq='h')  # Use lowercase 'h'

# Make predictions
forecast = model.predict(future)

# Plot forecast
fig = model.plot(forecast)
plt.title('Traffic Volume Forecast for Sector 17')
plt.xlabel('Time')
plt.ylabel('Vehicle Count')
plt.show()
