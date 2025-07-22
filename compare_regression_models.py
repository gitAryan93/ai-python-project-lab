import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Create noisy data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
# Slightly noisy y = x^2
y = np.array([1.2, 3.8, 9.1, 15.5, 25.1, 35.8, 49.9, 63.3, 81.7])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X, y)
y_linear_pred = linear_model.predict(X)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_poly_pred = poly_model.predict(X_poly)

# Evaluation
print("Linear R2:", r2_score(y, y_linear_pred))
print("Polynomial R2:", r2_score(y, y_poly_pred))

# Plotting
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_linear_pred, color='green', label='Linear Fit')
plt.plot(X, y_poly_pred, color='red', label='Polynomial Fit')
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.show()
