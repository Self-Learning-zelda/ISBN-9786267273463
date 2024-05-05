# ch23_25.py
import numpy as np

x1 = np.arange(6).reshape(2,-1)
print(f"陣列 1 \n{x1}")
x2 = np.arange(6,12).reshape(2,-1)
print(f"陣列 2 \n{x2}")
y = np.stack((x1,x2))
print(f"axis = 0 合併結果 \n{y}")


















 
