import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Input data (Study Hours vs Exam Scores)
X = np.array([[1], [2], [3], [4], [5]])  # Study Hours
y = np.array([50, 55, 65, 70, 75])      # Exam Scores

# Step 2: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Make predictions
predictions = model.predict(X)

# Step 4: Print model details
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² Score:", model.score(X, y))

# Step 5: Visualize results
plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X, predictions, color='red', linewidth=2, label='Predicted Line')
plt.title("Linear Regression: Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
