import numpy as np
from sklearn.linear_model import LinearRegression

# Example features: [study hours, sleep hours]
X = np.array([
    [2, 6],
    [3, 5],
    [4, 5],
    [5, 4],
    [6, 3]
])

# Target: exam score
y = np.array([60, 65, 70, 75, 80])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
predicted = model.predict(X)

# Output
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predicted Scores:", predicted)
print("R² Score:", model.score(X, y))
