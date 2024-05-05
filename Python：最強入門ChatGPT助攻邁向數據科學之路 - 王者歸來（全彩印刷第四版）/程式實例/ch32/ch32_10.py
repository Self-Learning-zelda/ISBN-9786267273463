# ch32_10.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
plt.scatter(data[:,0], data[:,1], c=label, cmap='bwr')
plt.grid(True)
plt.show()









