import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Create 3D synthetic data
np.random.seed(42)
X = np.random.rand(100, 3)

# Apply PCA to reduce to 2D
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Plot
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], alpha=0.7)
plt.title("PCA: 3D Data Reduced to 2D")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()
