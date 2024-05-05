# ch32_7.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model

np.random.seed(3)                                   # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100,
                                n_features=1,
                                noise=20)
# 數據分割為x_train,y_train訓練數據, x_test,y_test測試數據
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

e_model = linear_model.LinearRegression()           # 建立線性模組物件
e_model.fit(x_train, y_train)
print(f'斜率  = {e_model.coef_[0].round(2)}')
print(f'截距  = {e_model.intercept_.round(2)}')

















