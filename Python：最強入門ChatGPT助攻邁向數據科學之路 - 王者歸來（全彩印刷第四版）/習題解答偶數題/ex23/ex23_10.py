# ex23_10.py
import numpy as np

x1 = np.arange(6).reshape(2,-1)
print(f"陣列 1 \n{x1}")
x2 = np.arange(6,12).reshape(2,-1)
print(f"陣列 2 \n{x2}")
y1 = np.hstack((x1,x2))
print(f"水平合併結果 \n{y1}")
y2 = np.vstack((x1,x2))
print(f"垂直合併結果 \n{y2}")

















 
