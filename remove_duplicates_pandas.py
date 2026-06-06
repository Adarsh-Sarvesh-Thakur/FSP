import pandas as pd

data = {
    'ID': [1, 2, 3, 2, 4, 3],
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David', 'Charlie'],
    'Marks': [85, 90, 78, 90, 88, 78]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nDuplicate Rows:")
print(df.duplicated())

print("\nDuplicate Entries:")
print(df[df.duplicated()])

df_no_duplicates = df.drop_duplicates()

print("\nDataset after Removing Duplicates:")
print(df_no_duplicates)
