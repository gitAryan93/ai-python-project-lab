import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
data = {
    'Hours_Studied': [2, 4, 6, 8, 10],
    'Practice_Problems': [5, 10, 20, 25, 30],
    'Score': [50, 60, 65, 80, 95]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Hours_Studied', 'Practice_Problems']]
y = df['Score']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Predictions:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared Score:", r2_score(y_test, y_pred))
