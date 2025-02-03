import pandas as pd

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

df_confirmed = pd.read_csv(url_confirmed)
df_deaths = pd.read_csv(url_deaths)

#Delete unneccessary column
df_confirmed = df_confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
df_confirmed = df_confirmed.groupby('Country/Region').sum()

df_deaths = df_deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
df_deaths = df_deaths.groupby('Country/Region').sum()

df_confirmed = df_confirmed.transpose()
df_deaths = df_deaths.transpose()

df_confirmed.index = pd.to_datetime(df_confirmed.index)
df_deaths.index = pd.to_datetime(df_deaths.index)
