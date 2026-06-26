import pandas as pd
import numpy as np

# Loading Data from Local CSV File
df = pd.read_csv('orders.csv')
print(f"Successfully loaded {len(df)} records.")
print("\nInitial Data:")
print(df)

# Cleaning missing fields and formatting timestamps
df['delivery_issue'] = df['delivery_issue'].fillna("Unreported Issue")
df = df.dropna()

df['delivery_date'] = pd.to_datetime(df['delivery_date'])
print("\nData after formatting dates and handling null values:")
print(df)
print("Total records after dropping null values:", len(df))

# Using NumPy to calculate delivery delays
current_date = pd.Timestamp("2026-06-26")
df["delay_days"] = (current_date - df['delivery_date']).dt.days
df["is_delayed"] = np.where(df["delay_days"]>0, 1, 0)
print("\nCleaned and Processed Customer Order Insights Data:")
print(df.to_string(index=False))

# Top delayed customers and most common delivery issues
print(("\nTop delayed Customers:"))
print(df.groupby(["customer_id", "customer_name"])["is_delayed"].sum().reset_index())

print("\n Most Common Delivery Issues:")
delivery_issues = df.groupby('delivery_issue')['is_delayed'].size().reset_index(name='incident_count')
delivery_issues = delivery_issues.sort_values(by='incident_count', ascending=False)
print(delivery_issues)