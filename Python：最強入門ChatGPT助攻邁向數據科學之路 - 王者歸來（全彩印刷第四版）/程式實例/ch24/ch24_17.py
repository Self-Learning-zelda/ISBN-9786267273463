# ch24_17.py
import matplotlib.pyplot as plt
import numpy as np

mu = 0                                                  # 平均值
sigma = 1                                               # 標準差
s = np.random.randn(10000)                              # 隨機數
print(s)

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()












