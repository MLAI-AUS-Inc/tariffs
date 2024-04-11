# pip install matplotlib pandas
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('training_data.csv')


wanted_columns = ['timestamp', 'price', 'pv_power', 'temperature', 'demand', 'pv_power_basic', 'pv_power_forecast_1h',
       'pv_power_forecast_2h',
       'pv_power_forecast_24h',]

final_columns = ['timestamp', 'temp_air', 'price', 'pv_power', 'demand', 'pv_power_basic', 'pv_power_forecast_1h',
       'pv_power_forecast_2h',
       'pv_power_forecast_24h',]


df = df[final_columns]

print(df.head(10))

print(df['pv_power_basic'].describe())
# align timestamp to UTC+10
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['timestamp'] = df['timestamp'] + pd.Timedelta(hours=10)

df[-1000:].plot(x='timestamp', y=['pv_power', 'demand', 'price'], secondary_y='pv_power', figsize=(20, 10))
plt.show()