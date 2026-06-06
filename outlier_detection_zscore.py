import numpy as np

data = [10, 12, 15, 18, 20, 22, 25, 100]

mean = np.mean(data)
std_dev = np.std(data)

print("Dataset:", data)
print("Mean =", mean)
print("Standard Deviation =", std_dev)

outliers = []

for x in data:
    z_score = (x - mean) / std_dev
    print(f"Value: {x}, Z-Score: {z_score:.2f}")

    if abs(z_score) > 2:
        outliers.append(x)

print("\nOutliers:", outliers)
