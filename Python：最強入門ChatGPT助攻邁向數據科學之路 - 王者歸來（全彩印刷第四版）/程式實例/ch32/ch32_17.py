# ch32_17.py
from sklearn import datasets

data, label = datasets.load_iris(return_X_y=True)
print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")













