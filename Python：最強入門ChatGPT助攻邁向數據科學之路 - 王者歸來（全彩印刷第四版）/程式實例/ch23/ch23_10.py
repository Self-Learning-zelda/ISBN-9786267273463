# ch23_10.py
import numpy as np

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
print("建議用此方法")
print(f"x4[2,1] = {x4[2,1]}")
print(f"x4[1,3] = {x4[1,3]}")
print("也可以用下列方法")
print(f"x4[2][1] = {x4[2][1]}")
print(f"x4[1][3] = {x4[1][3]}")














 
