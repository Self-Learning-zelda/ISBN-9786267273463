# ch32_18.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(data,
                   label,test_size=0.2,random_state=0)
# 建立分類模型                                             
tree_model = DecisionTreeClassifier()
# 建立訓練數據模型
tree_model.fit(dx_train, label_train)
# 對測試數據做預測
y_pred = tree_model.predict(dx_test)
print(f"測試的真實分類\n{label_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("-"*70)

# 輸出準確性
print(f"訓練資料的準確性 = {tree_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {tree_model.score(dx_test, label_test)}")









