from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load iris dataset
iris = load_iris()
X = iris.data

# Cluster
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_

# Reduce dimensions for plotting
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.title("KMeans Clustering on Iris Data (PCA Reduced)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
