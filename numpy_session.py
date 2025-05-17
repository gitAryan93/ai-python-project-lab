import numpy as np

# Original data
data = np.array([12, 8, 14, 10, 6, 11, 9])
print("Original Data:", data)

# Basic stats
print("Mean:", np.mean(data))                  # Average
print("Median:", np.median(data))              # Middle value
print("Standard Deviation:", np.std(data))     # Spread
print("Max:", np.max(data))                    # Highest value
print("Min:", np.min(data))                    # Lowest value

middle_slice = data[2:5]
print("Middle 3 values:", middle_slice)

# Mean of middle slice
print("Mean of middle slice:", np.mean(middle_slice))

# Values greater than the overall mean
mean_val = np.mean(data)
above_mean = data[data > mean_val]
print("Values above mean:", above_mean)
print("How many above mean:", len(above_mean))

# BONUS: Reshape
reshaped_row = data.reshape(1, 7)  # 1 row, 7 columns
reshaped_col = data.reshape(7, 1)  # 7 rows, 1 column

print("\nReshaped to 1x7:\n", reshaped_row)
print("Reshaped to 7x1:\n", reshaped_col)
