# ch32_16_1.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 載入鳶尾花數據集
iris = datasets.load_iris()

# 將特徵和目標變數分開
X = iris.data
y = iris.target

# 將數據分為訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 特徵縮放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 建立 SVM 分類器
svm_classifier = SVC(kernel='rbf', C=1.0, random_state=9)

# 使用訓練數據擬合模型
svm_classifier.fit(X_train_scaled, y_train)

# 進行預測
y_pred = svm_classifier.predict(X_test_scaled)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)

# 計算準確度
accuracy = accuracy_score(y_test, y_pred)
print("準確度 :", accuracy)



