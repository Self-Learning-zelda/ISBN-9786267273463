# ch35_1.py
from sklearn import datasets

# 載入葡萄酒數據集
wine = datasets.load_wine()

print(f"自變數  樣本外形 : {wine.data.shape}")
print(f"目標變數樣本外形 : {wine.target.shape}")

# 輸出第一筆自變數
print("自變數 特徵值")
print(wine.data[0])

# 輸出第一筆目標變數, 分類
print("目標變數 葡萄酒品種")
print(wine.target[0])
