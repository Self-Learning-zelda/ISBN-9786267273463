# ch36_2.py
import seaborn as sns

# 讀取Seaborn模組的Titanic數據集
titanic_data = sns.load_dataset('titanic')

# 輸出資料訊息
print(titanic_data.info())
print("-"*70)

# 輸出第一筆資料
print("第 1 筆資料內容")
print(titanic_data.iloc[0])



