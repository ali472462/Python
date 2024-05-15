#                  ////////////////     Handle Missing Data      ////////////////
import numpy as np
import pandas as pd
data = {
    "Date": ["2023-08-01", "2023-08-02", "2023-08-05", "2023-08-06", "2023-08-07", "2023-08-08", "2023-08-09", "2023-08-10"],
    "Temperature (°F)": [82, 79, 90, 86, 81, np.nan, 77, 80],
    "Humidity (%)": [65, 72, 55, 70, 75, 68, 62, np.nan],
    "Precipitation": [0.02, 0.08, 0.00, np.nan, 0.05, 0.10, 0.01, 0.00]
}
df = pd.DataFrame(data)
df.to_excel("../files/weather_new_york.xlsx", index=False)
#df=pd.read_excel("../files/weather_new_york.xlsx",parse_dates=["Date"])
print(df.set_index('Date',inplace=True))
print(type(df.Precipitation[0]))
df_new=df.fillna(method="ffill",axis="columns")
#print(f"{df}\n{df_new}")
print(df_new.interpolate())
print(df_new.dropna(thresh=2))

import pandas as pd
import numpy as np
data = {
    "Date": ["2023-08-01", "2023-08-02", "2023-08-03", "2023-08-04", "2023-08-05", "2023-08-06", "2023-08-07", "2023-08-08", "2023-08-09", "2023-08-10"],
    "Temperature (°F)": [82, 79, 75, 74, 90, 86, 81, 79, 77, 80],
    "Humidity (%)": [65, 72, 68, 70, 55, 70, 75, 71, 62, 66],
    "Precipitation": [0.02, 0.08, 0.03, 0.00, 0.00, 0.01, 0.05, 0.09, 0.02, 0.00]
}

df = pd.DataFrame(data)
df.to_excel("../files/weather_new_york.xlsx", index=False)

                           # Read the Excel file into a DataFrame
df = pd.read_excel("../files/weather_new_york.xlsx")
print(df)
                          # Drop specific rows (3 and 4)
rows_to_drop = [3, 4]
df = df.drop(rows_to_drop)
print(df)
                           # Convert the "Date" column to a datetime dtype
df["Date"] = pd.to_datetime(df["Date"])

# Set "Date" as the index
df.set_index("Date", inplace=True)
print(df)
                            # Reindex with a new date range
date_range = pd.date_range(start="2023-08-01", end="2023-08-10", freq="D")
df = df.reindex(date_range)
print(df.dropna())

print(df)

                             # Forward-fill missing values
df_filled = df.fillna(method="ffill")

print(df_filled)
