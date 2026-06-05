import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)
print(arr + 5)
print(arr * 2)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(arr.shape)

# 2D Array
arr = np.array([[10, 20, 30],
               [40, 50, 60]])
print(arr)
print(arr.shape)

# Easy ways to create arrays (mostly used in machine learning)
arr = np.zeros((3, 4))
print(arr)
arr = np.ones((2, 3))
print(arr)
arr = np.arange(1,11)
print(arr)
arr = np.arange(1,11,2)
print(arr)
arr = np.arange(5)
print(arr)

import pandas as pd

data = {
    "employee_id": [101, 102, 103],
    "name": ["Rahul", "Priya", "Amit"],
    "salary": [75000, 85000, 65000]
}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv("employees.csv")
print(df)
print(df.head()) # First 5 rows
print(df.tail()) # Last 5 rows
print(df.dtypes) # Shows the datatype of each column
print(df.info()) # Summary
print(df.describe()) # Statistical Information
print(df["name"])
print(df[
          ["name", "salary"]
      ])
