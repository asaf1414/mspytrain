###############
# Data preparation for 2011
###############
# Data Source: https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# Save this data as a separate file by year
import numpy as np
import pandas as pd
df_2011 = pd.read_csv('C:\\Labs\\Module1\\LAB\\M01_L02_Lab02\\BikeRentalCY2011.csv')
df_2011.set_index(['instant'], inplace=True)

###############
# Data preparation for 2012
###############
df_2012 = pd.read_csv('C:\\Labs\\Module1\\LAB\\M01_L02_Lab02\\BikeRentalCY2012.csv')
df_2012.set_index(['instant'], inplace=True)
df = df_2011.append(df_2012)

###############
# Data preparation for weather situation
###############
weather = pd.read_csv('C:\\Labs\\Module1\\LAB\\M01_L02_Lab02\\WeatherSituation.csv')
data = df.merge(weather, left_on='weathersit', right_on='code')
data.drop('code', axis=1, inplace=True)
data.head()

###############
# Clean missing data
###############
data.isnull().any()
data[data['season'].isnull()]
data[data['dteday'] == '2011/1/2'].head()
data.loc[data['season'].isnull(), 'season'] = 1
data.isnull().any()

###############
# Processing data
###############
data['cnt'] = data['casual'] + data['registered']
data['casual ratio'] = data['casual'] / data['cnt']

###############
# Calculate basic statistics
###############
data[['temp', 'hum', 'windspeed','casual','registered', 'casual ratio']].describe()

###############
# Aggregation
###############
data.groupby(['dteday']).aggregate(['sum', 'min','max', np.std])['cnt']
data.groupby(['hr']).aggregate(['sum', 'min','max', np.std])['cnt']
data.groupby(['yr', 'mnth']).aggregate(['sum', 'min','max', np.std])['cnt']
