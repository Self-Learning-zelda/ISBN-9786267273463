# ch23_21.py
import numpy as np

x = np.arange(16)
print(f"原陣列 x = {x}")
y = np.reshape(x,(-1,8))
print("新陣列 y =")
print(y)
print(f"原陣列 x = {x}")




