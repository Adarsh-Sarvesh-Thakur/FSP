# List of values
values = [12, 25, 40, 55, 70]

x_min = min(values)
x_max = max(values)

normalized_values = []

for x in values:
    x_norm = (x - x_min) / (x_max - x_min)
    normalized_values.append(x_norm)

print("Original Values:", values)
print("Normalized Values:", normalized_values)
