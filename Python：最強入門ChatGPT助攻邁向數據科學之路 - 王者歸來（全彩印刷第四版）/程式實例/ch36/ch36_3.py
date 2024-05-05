# ch36_3.py
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# 下載鐵達尼號數據集
titanic_data = sns.load_dataset('titanic')
# 數據預處理, 分別是刪除欄位, 缺失值補上中位數年齡
titanic_data.drop(['deck', 'embark_town', 'alive', 'class', 'who',
                   'adult_male', 'alone'], axis=1, inplace=True)        
titanic_data['age'].fillna(titanic_data['age'].median(), inplace=True)
# 數據預處理, 用眾數取代缺失值, 這裡假設只有一個眾數
titanic_data['embarked'].fillna(titanic_data['embarked'].mode()[0], inplace=True)
# 對類別特徵進行one-hot編碼
titanic_data = pd.get_dummies(titanic_data, columns=['sex', 'embarked'])

# 劃分數據集
X = titanic_data.drop('survived', axis=1)   # X 數據及捨去 survived 欄位 - train
y = titanic_data['survived']                # survived 欄位當作 y 數據集 - test
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

# 建立 Logistic Regression 模型
model = LogisticRegression(max_iter=1000, random_state=9)
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)
print(f"測試的真實分類\n{y_test}")
print("-"*70)
print(f"預測的目標分類\n{y_pred}")
print("="*70)

# 評估模型
print(f"準確率(Accuracy Score) : {accuracy_score(y_test, y_pred):.2f}")
print("-"*70)
print("混淆矩陣(Confusion Matrix):")
print(confusion_matrix(y_test, y_pred))
print("-"*70)
print("分類報告(Classification Report):")
print(classification_report(y_test, y_pred))

