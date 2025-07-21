from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load digits
X, y = load_digits(return_X_y=True)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

# Model
model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Report
print("Classification Report:\n")
print(classification_report(y_test, y_pred))
