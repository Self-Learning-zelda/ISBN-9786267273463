# ex32_2.py
from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24]
y = [50,30,25,20,15,20,30,40,58,62,77,90,100,125,128,130,150,120,88,95,97,80]

coef = np.polyfit(x, y, 3)                          # 迴歸直線係數
model = np.poly1d(coef)                             # 線性迴歸方程式
print(f"18點購物人數預測 = {model(15).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")


















