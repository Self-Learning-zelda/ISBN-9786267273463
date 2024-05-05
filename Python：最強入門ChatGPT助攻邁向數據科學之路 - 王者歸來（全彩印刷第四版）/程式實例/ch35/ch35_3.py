# ch35_3.py
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 載入葡萄酒數據集
wine_data = load_wine()
X = wine_data.data
y = wine_data.target

# 將數據集分為訓練集和測試集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 建立KNN分類器，設定n_neighbors為5
knn = KNeighborsClassifier(n_neighbors=5)

# 使用訓練集訓練KNN分類器
knn.fit(X_train, y_train)

# 使用KNN分類器對測試集進行預測
y_pred = knn.predict(X_test)

print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)
print(f"訓練資料的準確性 = {knn.score(X_train, y_train).round(2)}")
print(f"測試資料的準確性 = {knn.score(X_test, y_test).round(2)}")


