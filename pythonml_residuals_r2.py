import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])  # Imperfect line

# Model
model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)

# Residuals
residuals = y - predicted

# Output
print("Actual:", y)
print("Predicted:", predicted)
print("Residuals:", residuals)
print("R² Score:", r2_score(y, predicted))
