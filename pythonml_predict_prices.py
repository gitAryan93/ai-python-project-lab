import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Fake dataset (price prediction)
data = {
    'bedrooms': [2, 3, 4, 3, 5, 2, 4, 3, 5, 6],
    'bathrooms': [1, 2, 2, 1, 3, 1, 2, 1, 3, 4],
    'size_sqft': [1000, 1500, 1800, 1200, 2500, 1100, 1600, 1300, 2400, 2800],
    'price_k': [200, 300, 350, 250, 500, 220, 340, 260, 480, 550]
}
df = pd.DataFrame(data)

X = df[['bedrooms', 'bathrooms', 'size_sqft']]
y = df['price_k']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)

# Output
print("Actual Prices:", y_test.values)
print("Predicted Prices:", predicted)
print("R² Score:", r2_score(y_test, predicted))
