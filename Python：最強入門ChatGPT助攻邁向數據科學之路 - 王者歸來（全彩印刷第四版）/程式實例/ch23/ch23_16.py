# ch23_16.py
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
a = x[2:6]
b = x[[2,6]]
print(f"np.shares_memory(x,a) = {np.shares_memory(x,a)}")
print(f"np.shares_memory(x,b) = {np.shares_memory(x,b)}")


















 
