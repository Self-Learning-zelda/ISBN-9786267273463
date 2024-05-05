# ch37_2.py
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 加載糖尿病數據集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 將數據集分為訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 創建線性回歸模型並擬合數據
model = LinearRegression()
model.fit(X_train, y_train)

# 用測試集預測目標值
y_pred = model.predict(X_test)

# 計算模型的性能指標
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 輸出線性回歸模型的係數和截距
print(f"係數 : {model.coef_.round(2)}")
print(f"截距 : {model.intercept_:.2f}")
print("-"*70)
print(f"測試的真實值\n{y_test}")
print("-"*70)
print(f"預測的目標值\n{y_pred.round(1)}")
print("-"*70)

# 輸出模型性能指標
print(f"Mean Squared Error (MSE) : {mse:.2f}")
print(f"R^2 Score : {r2:.2f}")




