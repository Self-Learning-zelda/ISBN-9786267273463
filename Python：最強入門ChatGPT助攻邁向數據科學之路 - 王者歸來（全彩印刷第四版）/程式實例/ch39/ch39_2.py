# ch39_2.py
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 加載數據集
digits = load_digits()
X = digits.data
y = digits.target

# 劃分訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 選擇機器學習模型
model = RandomForestClassifier(random_state=9)

# 訓練模型
model.fit(X_train, y_train)

# 預測測試集
y_pred = model.predict(X_test)
print(f"測試的真實值\n{y_test}")
print("-"*70)
print(f"預測的目標值\n{y_pred.round(1)}")
print("-"*70)

# 計算 accuracy
acc = accuracy_score(y_test, y_pred)
print(f"準確率(Accuracy Score) : {acc:.2f}")
print("-"*70)

# 生成分類報告
report = classification_report(y_test, y_pred)
print("分類報告(Classification Report):")
print(report)



