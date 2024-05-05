# ch32_16.py
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

data, label = make_moons(n_samples=200,noise=0.2,random_state=0)

d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm_model = LinearSVC()
svm_model.fit(dx_train, label_train)
pred = svm_model.predict(dx_test)
# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print("="*50)
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測                                             
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)
# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")







