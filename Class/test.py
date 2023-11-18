# import libraries
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# Show plots in the notebook
%matplotlib inline

#import data
data = xr.open_dataset("NOAA_NCDC_ERSST_v3b_SST.nc", engine="netcdf4")
# check data
data

# slice the area needed (5N-5S, 170W-120W)
data = data.sel(lat=slice(-5,5), lon=slice(190, 240))
# check data
data

# check null values
data.isnull().sum()

# calculate the mean of the data according to time
mean_time = data.mean(dim=['lat', 'lon'])
#check mean_time
mean_time

# calculate the mean of the data according to month
mean_month = mean_time.groupby('time.month').mean()
# check result
mean_month

# find the anomalies
anomalies =mean_time.groupby('time.month') - mean_month
# check result
anomalies

# calculate the rolling mean
mean_rolling = anomalies.rolling(time=3, center=True, min_periods=1).mean()
# check result
mean_rolling

# transform to dataframe to plot, I am inspired by my roommate Zhouzhou
tf = mean_rolling.to_dataframe().reset_index()
anomalies_df = anomalies.to_dataframe().reset_index()
# check  result
tf

# check result
anomalies_df

plt.figure(figsize=(10,8), dpi=120)

# adjust the color
colour = np.where(anomalies_df['sst']>0,'red', 'skyblue')
# plot bar chart
ax = anomalies_df.plot(kind='bar', x='time', y='sst',legend= False, color=colour)
ax.plot( tf['time'], tf['sst'])

# adjust the x label
# 5 years a tick
year_index = anomalies_df['time'].dt.year[::60].index
year = anomalies_df['time'].dt.year[::60]
# set ticks and horizontal axis
ax.set_xticks(ticks=year_index, labels=year, rotation=0)
ax.set_xlabel('Year')



plt.figure(figsize=(10,8), dpi=120)

# adjust the color
colour = np.where(anomalies_df['sst']>0,'red', 'skyblue')
# plot bar chart
ax = anomalies_df.plot(kind='bar', x='time', y='sst',legend= False, color=colour)
ax.plot( anomalies_df['time'], anomalies_df['sst'])

# adjust the x label
# 5 years a tick
year_index = anomalies_df['time'].dt.year[::60].index
year = anomalies_df['time'].dt.year[::60]
# set ticks and horizontal axis
ax.set_xticks(ticks=year_index, labels=year, rotation=0)
ax.set_xlabel('Year')


# 绘制柱状图
plt.bar(anomalies_df['time'], anomalies_df['sst'], color=colour)
plt.show()