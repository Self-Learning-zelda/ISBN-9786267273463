# ch32_5.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)                           # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100,
                                n_features=1,
                                noise=20)
# 數據分割為x_train,y_train訓練數據, x_test,y_test測試數據
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  
plt.rcParams["axes.unicode_minus"] = False  # 可以顯示負號
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train,y_train,label="訓練數據")
plt.scatter(x_test,y_test,label="測試數據")
plt.legend()
plt.show()















