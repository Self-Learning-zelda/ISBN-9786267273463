# ch37_3.py
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# 加載糖尿病數據集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 將數據集分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9)

# 數據標準化
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

y_train = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
y_test = scaler_y.transform(y_test.reshape(-1, 1)).ravel()

# 創建支持向量機回歸模型並擬合數據
model = SVR(kernel='linear', C=1)
model.fit(X_train, y_train)

# 用測試集預測目標值
y_pred = model.predict(X_test)

# 將預測值轉換回原始尺度
y_test = scaler_y.inverse_transform(y_test.reshape(-1, 1)).ravel()
y_pred = scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()

# 計算模型的性能指標
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 輸出模型性能指標
print(f"Mean Squared Error (MSE) : {mse:.2f}")
print(f"R^2 Score : {r2:.2f}")

