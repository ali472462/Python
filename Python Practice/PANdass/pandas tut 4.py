#REAd csv file
#WRITE csv file
#REAd excel file
#WRITE excel\xlsx file
import pandas as pd
import numpy as np
import random
# Generate random stock market data
#                               ///////////WRITE////////////
np.random.seed(42)
data = {
    'Stock': [f'Stock{i}' for i in range(1, 6)],
    'Price': np.random.randint(50, 153, 5),
    'Volume': np.random.randint(10000, 50000, 5),
    'PE Ratio': np.random.uniform(10, 30, 5),
    'Dividend Yield': np.random.uniform(0.5, 3.0, 5)
}
# Create a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to an CSV file
file_path = '../files/stock.csv'
df.to_csv(file_path, index=False)
#                               ///////////READ CSV////////////
df=pd.read_csv("../files/stock.csv")
print(df.head())
#                               ///////////WRITE XLSX////////////

# Generate random weather data
np.random.seed(42)

weather1 = {
    'Date': pd.date_range(start='2023-08-01', periods=5),
    'Temperature (Celsius)': np.random.randint(15, 35, 5),
    'Humidity (%)': np.random.randint(40, 80, 5),
    'Wind Speed (km/h)': np.random.randint(5, 20, 5),
    'Rainfall (mm)': [round(random.uniform(0, 15), 2) for _ in range(5)],
}
# Create a DataFrame
df = pd.DataFrame(weather1)
# Save the DataFrame to an Excel file
file_path = '../files/weather1.xlsx'
df.to_excel(file_path, index=False)
#                               ///////////READ XLSX////////////
df=pd.read_excel('../files/weather1.xlsx')
print(f"{df}")



#                   /////////////////////CHACHA LECTURE//////////////////////
df = pd.read_csv('../files/output.csv', na_values={
        'PB Ratio': ['n.a.', "not available", -1],
        'PE Ratio': ['n.a.', "not available", -1]})
print(f"Reading Output.csv File \n{df}")

#                           //////////////////Witing to csv///////////////////
df.to_csv("../files/new.csv", index=False)
print(df.columns)
print(df.to_csv("../files/new.csv",columns=["Company Name","PE Ratio"],header=False,index=False))
#                           //////////////////Witing to Excel///////////////////
def not_Avail(cell):
    if cell == "not available":
        return None
    return cell
df=pd.read_excel("../files/outpute.xlsx" , "Sheet1" , converters = {
    'PE Ratio':not_Avail,
    'PB Ratio':not_Avail } )
print(df.columns)
df.to_excel("../files/new.xlsx", columns=["PE Ratio","PB Ratio","Company Name"],index=False,startrow=2,startcol=2 )

#                           ///////////////Adding data in 2 excel shgeets///////////////////

weather_data = {'Date': ['2023-08-01', '2023-08-02'],
                'Temperature (C)': [28, 30],
                'Humidity (%)': [65, 70]}
weather_df = pd.DataFrame(weather_data , index=None)

# Create the stock dataframe
stock_data = {'Date': ['2023-08-01', '2023-08-02'],
              'Company': ['ABC', 'XYZ'],
              'Stock Price': [150, 175]}
stock_df = pd.DataFrame(stock_data , index=None)
with pd.ExcelWriter("../files/new.xlsx") as writer:
    print(weather_df.to_excel(writer , sheet_name="Weather"))
    print(stock_df.to_excel(writer , sheet_name="Stocks"))