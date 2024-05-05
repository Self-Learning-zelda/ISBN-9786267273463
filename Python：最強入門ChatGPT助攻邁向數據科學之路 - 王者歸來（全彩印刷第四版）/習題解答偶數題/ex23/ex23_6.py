# ch23_6.py
import numpy as np

x = np.array([10,21,32,43,54,65,76,87,98,9])
print(f"原始的 x = {x}")        # 原始陣列
odd = (x%2 == 1)                # 建立奇數為True的布林值陣列
print(f"odd     = {odd}")       # 輸出布林值陣列
print(f"x[odd]  = {x[odd]}")    # 布林值切片
x[odd] = 0
print(f"最後的 x = {x}")        # 結果陣列














 
