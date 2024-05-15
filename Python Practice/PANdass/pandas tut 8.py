import pandas as pd
ind_weather_data = pd.DataFrame ({
    'Date': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Temperature_C': [30, 32, 29],
    'Humidity_%': [60, 55, 65],
    'Precipitation_mm': [0.2, 0.0, 0.5]
})
print(ind_weather_data)
pak_weather_data = pd.DataFrame ({
    'Date': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Temperature_C': [35, 34, 33],
    'Humidity_%': [50, 52, 48],
    'Precipitation_mm': [0.0, 0.1, 0.0]
})
print(pak_weather_data)
df=pd.concat([ind_weather_data,pak_weather_data],keys=['Ind','Pak'])  # """ignore_index=True"""

print(df)
print(df.loc['Ind'])

# Sample wind speed data
wind_speed_data = pd.DataFrame( {
    'Location': ['Location A', 'Location B', 'Location C'],
    'Day 1': [12.5, 8.2, 15.7],
    'Day 2': [10.8, 9.4, 16.2],
    'Day 3': [11.7, 7.9, 14.6]
},index=[1,2,3])

temperature_data = pd.DataFrame( {
    'Location': ['Location B', 'Location A', 'Location C'],
    'Day 1': [26.8, 27.3, 22.7],
    'Day 2': [25.0, 28.5, 23.2],
    'Day 3': [24.5, 25.7, 21.8]
},[2,1,3])

print(wind_speed_data,temperature_data)
df=pd.concat([wind_speed_data,temperature_data],keys=['Temp','Wind_S'],axis=1)
print(df)

#                        Series add in concatenate

s=pd.Series(['FSD','LHR','SRG'],name="event",index=[1,2,3])
df_new=pd.concat([df,s],axis=1)
print(df_new)