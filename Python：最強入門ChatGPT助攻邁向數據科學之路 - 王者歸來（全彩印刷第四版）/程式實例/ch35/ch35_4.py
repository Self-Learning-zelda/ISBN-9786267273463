# ch35_4.py
from sklearn.metrics import accuracy_score

# 假設我們已經有了實際目標變數值和模型預測的目標變數值
y_true = [1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 1, 1, 0, 1]

# 計算準確率
acc = accuracy_score(y_true, y_pred)
print(f"準確率 : {acc.round(2)}")









