import pandas as pd
import numpy as np

dates = pd.date_range(start="2024-01-01", periods=20, freq="D")
sales = [100, 120, np.nan, 130, 125, np.nan, np.nan, 140, 150, 160,
         np.nan, 170, 180, np.nan, 190, 200, np.nan, 210, 220, np.nan]

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

df.to_csv("timeseries_sales.csv", index=False)

print("File created!")