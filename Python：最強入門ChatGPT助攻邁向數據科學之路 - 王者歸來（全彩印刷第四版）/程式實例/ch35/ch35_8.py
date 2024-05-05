# ch35_8.py
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 加載葡萄酒數據集
wine = load_wine()

# 分割數據集
X_train,X_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size=0.2,random_state=9)

# 建立羅吉斯回歸分類器，使用 OvR 策略
log_reg = LogisticRegression(multi_class='ovr', max_iter=10000)

# 訓練分類器
log_reg.fit(X_train, y_train)

# 進行預測
y_pred = log_reg.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)

# 計算 accuracy
acc = accuracy_score(y_test, y_pred)
print(f"準確率(Accuracy Score) : {acc:.2f}")
print("-"*70)
# 生成分類報告
report = classification_report(y_test, y_pred)

print("分類報告(Classification Report):")
print(report)






