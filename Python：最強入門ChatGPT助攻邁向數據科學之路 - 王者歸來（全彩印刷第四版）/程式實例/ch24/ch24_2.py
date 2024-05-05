# ch24_2.py
import numpy as np

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
# 方法 1
print(f'平均消費金額 = {sum(x)/len(x)}')
# 方法 2
print(f'平均消費金額 = {np.mean(x)}')


