# ch32_26
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# 載入Iris數據集
iris = datasets.load_iris()
data = iris.data
true_labels = iris.target

# 設定K值
K = 3

# 使用K-means進行聚類
kmeans = KMeans(n_clusters=K, random_state=9)
kmeans.fit(data)

# 獲得聚類標籤
predicted_labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 計算調整蘭德係數（ARI）
ari = adjusted_rand_score(true_labels, predicted_labels)
print(f"Adjusted Rand Index (ARI) : {ari:.2f}")

# 繪製聚類結果（僅使用前兩個特徵繪製二維圖）
plt.scatter(data[:, 0], data[:, 1], c=predicted_labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title(f"Iris Clustering (ARI = {ari:.2f})")
plt.show()


