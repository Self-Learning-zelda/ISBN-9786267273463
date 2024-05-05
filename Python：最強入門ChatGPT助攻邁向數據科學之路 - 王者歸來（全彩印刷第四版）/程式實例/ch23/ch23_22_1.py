# ch23_22_1.py
import numpy as np

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
y = x.flatten()
print(y)
print(f"np.shares_memory(x,y) = {np.shares_memory(x,y)}")














 
