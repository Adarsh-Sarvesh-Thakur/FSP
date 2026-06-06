import numpy as np

data = [12, 25, 40, 55, 70]

mean = np.mean(data)
std_dev = np.std(data)

z_scores = []

for x in data:
    z = (x - mean) / std_dev
    z_scores.append(z)

print("Original Data:", data)
print("Mean =", mean)
print("Standard Deviation =", std_dev)
print("Z-Score Normalized Data:")

for i in range(len(data)):
    print(f"{data[i]} --> {z_scores[i]:.4f}")
