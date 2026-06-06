from sklearn.preprocessing import LabelEncoder

colors = ["Red", "Blue", "Green", "Blue"]

print("Original Data:")
print(colors)

encoder = LabelEncoder()
encoded_colors = encoder.fit_transform(colors)

print("\nEncoded Data:")
print(encoded_colors)

print("\nLabel Mapping:")
for color, label in zip(encoder.classes_, range(len(encoder.classes_))):
    print(f"{color} -> {label}")
