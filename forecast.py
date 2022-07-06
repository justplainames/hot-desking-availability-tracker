from matplotlib import pyplot as plt
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from dynamodb_json import json_util as json
import aws_controller

#df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
#print(df.head())

#Loading data into dataframe from DynamoDB
df = pd.DataFrame(json.loads(aws_controller.get_items()['Items']))

print(df.head())

#Reformatting data
df.drop(['ts'],axis=1,inplace=True)
print(df.head())

df.columns = ['ds','y']
print(df.head())

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

#Renaming Graph
fig1 = m.plot(forecast)
plt.ylabel('People')
plt.xlabel('Date Time')
fig2 = m.plot_components(forecast)
plt.ylabel('People')
plt.xlabel('Date Time')
fig1.savefig('Forecasting/test6.png')
fig2.savefig('Forecasting/test7.png')

plot_plotly(m, forecast)
plot_components_plotly(m, forecast)

#print(aws_controller.get_items()['Items'])
