import pandas as pd
import numpy as np
"""
# Create date range
date_range = pd.date_range(start="2023-08-01", periods=10, freq="D")

# Generate random weather data
np.random.seed(42)
temperature = np.random.randint(70, 95, size=10)
humidity = np.random.randint(40, 85, size=10)
precipitation = np.random.choice([0.0, 0.1, 0.2, np.nan], size=10)

# Create DataFrame
data = {
    "Date": date_range,
    "Temperature": temperature,
    "Humidity": humidity,
    "Precipitation": precipitation
}

df = pd.DataFrame(data)

# Save to Excel file
df.to_excel("../files/weather6.xlsx", index=False)
"""
df=pd.read_excel("../files/weather_new_york.xlsx")

df=df.replace({
    'Temperature': 80,
    'Humidity':75,
    'Precipitation':0.1
},np.NaN)
df_new=df.replace({
    "Precipitation": '[A-Z-a-z]'
},"",regex=True)
print(df_new)


import pandas as pd
import numpy as np

# Create data for the students
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Bob", "Charlie", "David", "Eve"],
    "Score 1": np.random.randint(0, 100, size=9)
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

df=df.replace(["Alice","Bob","Charlie","David","Eve"],[1,2,3,4,5])

print(df)