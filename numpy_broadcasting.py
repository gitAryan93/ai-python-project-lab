# Week 5 Day 1 - NumPy Broadcasting Practice
import numpy as np

# Scalar Broadcasting
a = np.array([1, 2, 3])
print("a + 5", a + 5)

# Row Broadcasting
a = np.array([[1, 2, 3],
             [4, 5, 6]])
b = np.array([10, 20, 30])
print("a + b", a + b)

# Failing Broadcasting
a = np.array([[1, 2],
             [3, 4]])
b = np.array([10, 20, 30])
try:
    print("Invalid broadcast:\n", a + b)
except ValueError as e:
    print("Broadcast failed:", e)
