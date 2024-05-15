"""import pandas as pd
import matplotlib.pyplot as plt  # Import the plotting module

df = pd.read_excel("../files/weather7.xlsx")
print(df)
g = df.groupby("City")
print(g.get_group("London"))
for city_name, city_data in g:
    print(city_name)
    print(city_data)
    print(city_data)  # Print describe() for each city group
    print(g.mean())
    print(f"{g.describe()}")
# Calculate and print average temperature for each city group
avg_temperatures = g["Temperature (°C)"].mean()
print(f"AVG Temperatures:\n{avg_temperatures}")

# Plot the data for each city group
for city_name, city_data in g:
    print(f"Plot for {city_name}:")
    city_data.plot(x='Date', y='Temperature (°C)', kind='line')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature in {city_name}')
    plt.show()
for city_n,city_d in g:
    print(f"Plot For{city_d}")
    city_d.plot(x="Temperature (°C)",y="Humidity (%)",kind="line")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.title(f"Temperature in {city_n}")
    plt.show()"""
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "City": ["New York", "New York", "New York", "Los Angeles", "Los Angeles", "Los Angeles", "London", "London", "London"],
    "Date": ["8/1/2023", "8/2/2023", "8/3/2023", "8/1/2023", "8/2/2023", "8/3/2023", "8/1/2023", "8/2/2023", "8/3/2023"],
    "Temperature (°C)": [28, 27, 25, 32, 31, 30, 22, 20, 19],
    "Humidity (%)": [60, 65, 70, 45, 50, 55, 80, 85, 90],
    "Wind Speed (km/h)": [10, 12, 15, 8, 10, 12, 20, 18, 22]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("../files/new.csv", index=False)

print("Data written to new.csv")
df = pd.read_csv("../files/new.csv")
print(df)

g = df.groupby("City")
print(g)

for city, data in g:
    print("City:",city)
    print("\n")
    print("data:",data)
print(g["Temperature (°C)"].mean())
print(g.describe())
print(g.size())
print(g.count())
"""
# Plot the temperature data for each city group
for city_name, city_data in g:
   # plt.figure()  # Create a new figure for each plot
    city_data.plot(x='Date', y='Temperature (°C)', kind='line')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature in {city_name}')
    plt.show()  # Display the plot
"""
# Create a line plot for Humidity vs. Temperature for each city group
for city_name, city_data in g:
    plt.plot(city_data["Humidity (%)"], city_data["Temperature (°C)"], label=f'{city_name} - Temperature')
    plt.plot(city_data["Humidity (%)"], city_data["Humidity (%)"], label=f'{city_name} - Humidity')
    plt.ylabel('Temperature (°C)')
    plt.title('Humidity vs. Temperature')
    plt.legend()
    plt.show()

def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'
g = df.groupby(lambda x: grouper(df, x, "Temperature (°C)"))
print(g)
for key, d in g:
    print("Group by Key: {}\n".format(key))
    print(d)


