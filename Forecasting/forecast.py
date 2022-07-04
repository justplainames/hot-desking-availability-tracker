import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
print(df.head())

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
fig1.savefig('Forecasting/test3.png')
fig2.savefig('Forecasting/test2.png')


plot_plotly(m, forecast)
plot_components_plotly(m, forecast)


