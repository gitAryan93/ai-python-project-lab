# Week 5 Day 1 - NumPy Indexing & Slicing
import numpy as np

# Basic Indexing
arr = np.array([10, 20, 30, 40, 50])
print("arr[0]:", arr[0])
print("arr[2]:", arr[2])
print("arr[-1]:", arr[-1])

# Basic Slicing
print("arr[1:4]", arr[1:4])
print("arr[:3]", arr[:3])
print("arr[2:]", arr[2:])

# Step Slicing
print("::2", arr[::2])
print("arr[1:5:2]", arr[1:5:2])
