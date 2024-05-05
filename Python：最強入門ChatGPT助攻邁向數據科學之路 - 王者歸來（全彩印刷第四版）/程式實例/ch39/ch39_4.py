# ch39_4.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 加載手寫數字數據集
digits = load_digits()
X = digits.data
y = digits.target

# 劃分訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 創建 PCA 實例，設定目標維度
pca = PCA(n_components=0.9, whiten=True)

# 使用訓練集擬合 PCA 模型
X_train_pca = pca.fit_transform(X_train)

# 使用擬合的 PCA 模型轉換測試集
X_test_pca = pca.transform(X_test)

# 創建並訓練隨機森林分類器
model = RandomForestClassifier(random_state=9)
model.fit(X_train_pca, y_train)

# 計算 accuracy
y_pred = model.predict(X_test_pca)
acc = accuracy_score(y_test, y_pred)
print(f"準確率(Accuracy Score) : {acc:.2f}")
print("-"*70)

# 生成分類報告
report = classification_report(y_test, y_pred)
print("分類報告(Classification Report):")
print(report)



