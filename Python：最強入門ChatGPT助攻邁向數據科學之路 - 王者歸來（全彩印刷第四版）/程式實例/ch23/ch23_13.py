# ch23_13.py
import numpy as np

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])
print("x[:,:]   = 結果是二維陣列")     # 結果是二維陣列
print(x[:,:])
print("-"*70)
print("x[2,:4]  = 結果是一維陣列")     # 結果是一維陣列
print(x[2,:4])
print("-"*70)
print("x[2,:]   = 結果是一維陣列")     # 結果是一維陣列
print(x[2,:])
print("-"*70)
print("x[:2,:1] = 結果是二維陣列")     # 結果是二維陣列    
print(x[:2,:1])
print("-"*70)
print("x[:,4:]  =  結果是二維陣列")    # 結果是二維陣列
print(x[:,4:])
print("-"*70)
print("x[:,4]   =  結果是一維陣列")    # 結果是一維陣列
print(x[:,4])












 
