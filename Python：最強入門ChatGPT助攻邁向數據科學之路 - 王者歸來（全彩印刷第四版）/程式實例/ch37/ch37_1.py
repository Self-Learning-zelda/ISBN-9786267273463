# ch37_1.py
from sklearn.datasets import load_diabetes

# 加載糖尿病數據集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 輸出數據集的形狀
print("X shape:", X.shape)
print("y shape:", y.shape)

# 輸出第一筆自變數（特徵）和目標變數
print("第一筆自變數（特徵）:", X[0])
print("第一筆目標變數      :", y[0])


