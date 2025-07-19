import numpy as np

# 1D Array
a = np.array([1, 2, 3, 4])
print("1D Array:\n", a)

# 2D Matrix
b = np.array([[1, 2,], [3, 4]])
print("2D Matrix:\n", b)

# Shape and data type
print("Shape of b:", b.shape)

# Element-wise operations
print("a + 10:", a + 10)
print("a squared:", a ** 2)

# Matrix multiplication
c = np.array([[5, 6], [7, 8]])
print("Matrix C:\n", c)
print("Dot product b · c:\n", np.dot(b, c))

# Reshape example
d = np.arange(1, 13)
print("Original array:", d)
print("Reshaped to 3x4:\n", d.reshape(3, 4))
