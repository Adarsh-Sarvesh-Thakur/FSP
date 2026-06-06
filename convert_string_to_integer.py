import pandas as pd

data = {
    'Numbers': ['10', '20', '30', '40', '50']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nData Type Before Conversion:")
print(df.dtypes)

df['Numbers'] = df['Numbers'].astype(int)

print("\nDataFrame After Conversion:")
print(df)

print("\nData Type After Conversion:")
print(df.dtypes)
