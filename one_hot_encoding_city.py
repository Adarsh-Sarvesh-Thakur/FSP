import pandas as pd

df = pd.DataFrame({
    'City': ['Kolkata', 'Delhi', 'Mumbai', 'Chennai']
})

print("Original Dataset:")
print(df)

encoded_df = pd.get_dummies(df, columns=['City'])

print("\nOne-Hot Encoded Dataset:")
print(encoded_df)
