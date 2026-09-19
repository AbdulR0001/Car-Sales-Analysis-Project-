
import pandas as pd
import numpy as np
rows = 100000
brands=["Toyota","Honda","Ford","BMW","Mercedes","Tesla","Audi","Nissan"]
countries=["Canada","USA","UK","Germany","Australia"]
fuel=["Gasoline","Diesel","Hybrid","Electric"]
dealers=["Dealer_A","Dealer_B","Dealer_C","Dealer_D"]
df=pd.DataFrame({
"Sale_ID":range(1,rows+1),
"Date":pd.date_range(start="2023-01-01", periods=rows, freq="h"),
"Brand":np.random.choice(brands,rows),
"Price":np.random.randint(20000,90000,rows),
"Fuel_Type":np.random.choice(fuel,rows),
"Country":np.random.choice(countries,rows),
"Dealer":np.random.choice(dealers,rows),
"Customer_Age":np.random.randint(18,70,rows),
"Gender":np.random.choice(["Male","Female"],rows)
})
df.to_csv('data/car_sales.csv', index=False)
print('Dataset created')
