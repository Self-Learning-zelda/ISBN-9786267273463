# ch23_7_2.py
import numpy as np

x = np.array([10,21,32,43,54,65,76,87,98,9])
print(f"原始的 x = {x}")        # 原始陣列
even = (x%2 == 0)               # 建立偶數為True的布林值陣列
print(f"even     = {even}")     # 輸出布林值陣列
print(f"x[even]  = {x[even]}")  # 布林值切片
x[even] = 0
print(f"最後的 x = {x}")        # 結果陣列














 
