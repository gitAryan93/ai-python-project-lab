# pythonml_confusion_matrix.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 1. Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 4. Predict on test data
y_pred = model.predict(X_test)

# 5. Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# 6. Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap='Blues')
plt.title("Confusion Matrix - Logistic Regression (Iris Dataset)")
plt.show()