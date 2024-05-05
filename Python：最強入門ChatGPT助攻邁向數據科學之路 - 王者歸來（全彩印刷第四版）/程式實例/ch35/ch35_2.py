# ch35_2.py
from sklearn import datasets

# 載入葡萄酒數據集
wine = datasets.load_wine()

# 輸出自變數
print("自變數 特徵值")
print(wine.data)

# 輸出目標變數, 葡萄酒品種
print("目標變數 葡萄酒品種")
print(wine.target)
