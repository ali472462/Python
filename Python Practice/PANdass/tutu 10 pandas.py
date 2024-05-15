import pandas as pd

df =pd.DataFrame( {
    'date': ['5/1/2017', '5/2/2017', '5/3/2017', '5/1/2017', '5/2/2017', '5/3/2017', '5/1/2017', '5/2/2017', '5/3/2017'],
    'city': ['new york', 'new york', 'new york', 'mumbai', 'mumbai', 'mumbai', 'beijing', 'beijing', 'beijing'],
    'temperature': [65, 66, 68, 75, 78, 82, 80, 77, 79],
    'humidity': [56, 58, 60, 80, 83, 85, 26, 30, 35]
})

print(df)

df_new=df.pivot(index="city",columns="date")
print(df_new)

df =pd.DataFrame( {
    'date': ['5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017', '5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017'],
    'city': ['new york', 'new york', 'new york', 'new york', 'mumbai', 'mumbai', 'mumbai', 'mumbai'],
    'temperature': [65, 61, 70, 72, 75, 78, 82, 80],
    'humidity': [56, 54, 60, 62, 80, 83, 85, 26]
})

df_new=df.pivot_table(index="date" , columns="city", aggfunc=("mean"),margins=True ) #Count fuc to tell total times used
print(f"Hello:{df_new}")
df["date"]=pd.to_datetime(df["date"])
print(type(df["date"][0]))
dff=df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')
print(dff)