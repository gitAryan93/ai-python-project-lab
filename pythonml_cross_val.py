from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load data
X, y = load_iris(return_X_y=True)

# Cross-validation
clf = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(clf, X, y, cv=5)

print(f"Cross-validation scores: {scores}")
print(f"Average accuracy: {scores.mean():.2%}")
