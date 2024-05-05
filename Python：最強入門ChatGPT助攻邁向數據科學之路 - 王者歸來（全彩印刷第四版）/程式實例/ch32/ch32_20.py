# ch32_20.py
import matplotlib.pyplot as plt
from sklearn import datasets

# 建立 300 個點, n_features=2, centers=3
data, label = datasets.make_blobs(n_samples=300, n_features=2,
                                  centers=3, random_state=10)                                

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False          # 可以顯示負號
# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:,0], data[:,1], marker="o", edgecolor="black")

plt.title("無監督學習",fontsize=16)
plt.show()















