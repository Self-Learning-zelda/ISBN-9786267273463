# ch32_23.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 創建一個簡單的12個二維數據點的資料集
data = np.array([[32, 3.5], [18, 0.9], [80, 15], [41, 4.8],
                 [25, 1.3], [55, 13],[70, 14.5], [33, 4.1],
                 [20, 1.9], [23, 1.7], [66, 12], [40, 3.8]])

# 設定K值
K = 3

# 使用scikit-learn的KMeans方法進行聚類
kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(data)

# 獲得聚類標籤和聚類中心
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 繪製結果
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*')
plt.title("無監督學習 - 捕獲魚的分類",fontsize=16)
plt.xlabel("身長")
plt.ylabel("體重")
plt.show()




