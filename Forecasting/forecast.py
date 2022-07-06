from matplotlib import pyplot as plt
import pandas as pd
from prophet import Prophet
from dynamodb_json import json_util as json
import aws_controller

#df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
#print(df.head())

#Loading data into dataframe from DynamoDB
df = pd.DataFrame(json.loads(aws_controller.get_items()['Items']))
print(df.head())

#Reformatting data
df.drop(['ts', 'device_name'], axis=1, inplace=True)
print(df.head())

df.columns = ['ds', 'y']
df['cap'] = 5
df['floor'] = 0
print(df.head())

m = Prophet(growth='logistic')
m.fit(df)

#Forecasting 30 days
future = m.make_future_dataframe(periods=30)
future['cap'] = 5
future['floor'] = 0
#future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

#print(forecast)

#Renaming Graph
fig1 = m.plot(forecast)
plt.ylabel('Crowd')
plt.xlabel('Date Time')
fig2 = m.plot_components(forecast)
plt.ylabel('Crowd')
plt.xlabel('Date Time')
fig1.savefig('static/images/Forecast_1.png')
fig2.savefig('static/images/Forecast_2.png')

#plot_plotly(m, forecast)
#plot_components_plotly(m, forecast)

#print(aws_controller.get_items()['Items'])

