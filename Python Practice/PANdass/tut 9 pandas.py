import pandas as pd


# Sample wind speed data
wind_speed_data = pd.DataFrame( {
    'City': ['London', 'Faisalabad', 'Karachi'],
    'Day 1': [12.5, 8.2, 15.7],
    'Day 2': [10.8, 9.4, 16.2],
    'Day 3': [11.7, 7.9, 14.6]
})

temperature_data = pd.DataFrame( {
    'City': ['London', 'Faisalabad', 'Delhi'],
    'Day 1': [26.8, 27.3, 22.7],
    'Day 2': [25.0, 28.5, 23.2],
    'Day 3': [24.5, 25.7, 21.8]
})

df=pd.merge(wind_speed_data,temperature_data , on="City", how="left",indicator=True )
print(df)


#Sufixes
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
print(df2)

df3=pd.merge(df1,df2,on="city",how="outer", suffixes=("_left","_Right") )
print(df3)