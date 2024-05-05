# ch37_4.py
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 加載糖尿病數據集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 將數據集分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 創建隨機森林回歸模型並擬合數據
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 用測試集預測目標值
y_pred = model.predict(X_test)

# 計算模型的性能指標
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# 輸出模型性能指標
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R^2 Score:", r2)
