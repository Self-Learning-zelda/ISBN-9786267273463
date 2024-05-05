# ch32_12.py
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data, label = make_blobs(n_samples=200,n_features=2,
                         centers=2,random_state=0)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
                                             
print(f"特徵數據外形 : {d_sta.shape}")
print(f"訓練數據外形 : {dx_train.shape}")
print(f"測試數據外形 : {dx_test.shape}")
print(f"標籤數據外形 : {label.shape}")
print(f"訓練數據外形 : {label_train.shape}")
print(f"測試數據外形 : {label_test.shape}")











