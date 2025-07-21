from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Multivariable dataset (e.g., [study_hours, sleep_hours])
X = np.array([
    [5, 7],
    [8, 6],
    [10, 8],
    [6, 5],
    [7, 9]
])
y = np.array([75, 80, 90, 70, 85])  # exam scores

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Results
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R² Score:", r2_score(y, y_pred))
