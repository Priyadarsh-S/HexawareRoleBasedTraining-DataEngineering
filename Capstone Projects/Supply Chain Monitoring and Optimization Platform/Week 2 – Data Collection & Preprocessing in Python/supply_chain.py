import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

# Loading Data from Local CSV File
df = pd.read_csv('supply_chain_data.csv')
print(f"Successfully loaded {len(df)} records.")
print("\nInitial Data:")
print(df)

# Cleaning Data using Pandas
df["delivery_date"] = pd.to_datetime(df["delivery_date"])
df = df.dropna()
print("\nData after formatting dates and dropping null values:")
print(df)
print("Total records after dropping null values:", len(df))

# Performing Basic Calculations using Numpy
current_timeline = pd.Timestamp("2026-06-16")
df["delay_days"] = (current_timeline - df["delivery_date"]).dt.days
df["delay_days"] = df["delay_days"].astype(int)

df["is_delayed"] = np.where(df["delay_days"]>0, "Yes", "No")

df["low_stock_risk"] = np.where(df["stock_level"]<15, "CRITICAL", "SAFE")

print("\nCleaned & Processed Supply Chain Data:")
final_data = df[[
    "order_id",
    "supplier_id",
    "item_name",
    "stock_level",
    "low_stock_risk",
    "delivery_date",
    "delay_days",
    "is_delayed",
    "status"
]]
print(final_data.to_string(index=False))