from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Visualize
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=iris.feature_names,
          class_names=iris.target_names)
plt.title("Decision Tree - Iris Dataset")
plt.show()
