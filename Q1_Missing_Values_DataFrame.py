import pandas as pd
import numpy as np

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [80, np.nan, 75, 90, np.nan],
    'Age': [20, 21, np.nan, 22, 23]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

df_mean = df.copy()
df_mean['Marks'].fillna(df_mean['Marks'].mean(), inplace=True)
df_mean['Age'].fillna(df_mean['Age'].mean(), inplace=True)

print("\nDataFrame after replacing missing values with Mean:")
print(df_mean)

df_median = df.copy()
df_median['Marks'].fillna(df_median['Marks'].median(), inplace=True)
df_median['Age'].fillna(df_median['Age'].median(), inplace=True)

print("\nDataFrame after replacing missing values with Median:")
print(df_median)

df_drop = df.dropna()

print("\nDataFrame after dropping rows with missing values:")
print(df_drop)
