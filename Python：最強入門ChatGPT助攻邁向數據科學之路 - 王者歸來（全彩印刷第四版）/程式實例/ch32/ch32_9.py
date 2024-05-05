# ch32_9.py
from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=5,n_features=2,
                         centers=2,random_state=0)
print(data)
print(f"分類 : {label}")






