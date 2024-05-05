# ch32_11.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
plt.scatter(d_sta[:,0], d_sta[:,1], c=label, cmap='bwr')
plt.grid(True)
plt.show()









