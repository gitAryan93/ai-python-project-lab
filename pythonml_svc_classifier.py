# pythonml_svc_classifier.py

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load data
digits = datasets.load_digits()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)

# SVC Model
svc = SVC(kernel='linear', C=1.0)
svc.fit(X_train, y_train)

# Predict
y_pred = svc.predict(X_test)

# Evaluate
print("SVC Classifier Report:")
print(classification_report(y_test, y_pred))
print(f"SVC Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
