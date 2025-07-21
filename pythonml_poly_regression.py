import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Input data (1D)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])  # Perfect square relation

# Polynomial transform
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)
predicted = model.predict(X_poly)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, predicted, color='red')
plt.title("Polynomial Regression (Degree 2)")
plt.xlabel("Input")
plt.ylabel("Target")
plt.grid(True)
plt.tight_layout()
plt.show()
