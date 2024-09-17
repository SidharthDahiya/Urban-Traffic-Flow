import pandas as pd
import plotly.express as px

# Load the dataset
traffic_data = pd.read_csv('chandigarh_traffic_data_september_2024_detailed.csv')
traffic_data['time'] = pd.to_datetime(traffic_data['time'])

# Create an interactive line plot
fig = px.line(traffic_data, x='time', y='vehicle_count', color='location',
              title='Traffic Flow Patterns Over Time',
              labels={'vehicle_count': 'Vehicle Count', 'time': 'Time'})

# Show the plot
fig.show()
