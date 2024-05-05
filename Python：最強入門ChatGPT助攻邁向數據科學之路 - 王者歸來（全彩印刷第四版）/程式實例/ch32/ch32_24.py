# ch32_24.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# 載入Iris數據集
iris = datasets.load_iris()
data = iris.data

# 設定K值
K = 3

# 使用scikit-learn的KMeans方法進行聚類
kmeans = KMeans(n_clusters=K, random_state=9)
kmeans.fit(data)

# 獲得聚類標籤和聚類中心
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 繪製結果（僅使用前兩個特徵繪製二維圖）
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()




