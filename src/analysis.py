
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/car_sales.csv')
print(df.head())
print(df.info())
print(df.describe())
df.drop_duplicates(inplace=True)
print('Total Revenue:', df['Price'].sum())
brand=df.groupby('Brand')['Price'].sum().sort_values(ascending=False)
country=df.groupby('Country')['Price'].sum().sort_values(ascending=False)
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.month
monthly=df.groupby('Month')['Price'].sum()
brand.to_csv('outputs/sales_by_brand.csv')
country.to_csv('outputs/sales_by_country.csv')
monthly.to_csv('outputs/monthly_sales.csv')
print('Analysis complete')
