# ch21_2.py
import json

listObj = [{'Name':'Peter', 'Age':25, 'Gender':'M'}]    # 串列元素是字典
jsonData = json.dumps(listObj)                          # 串列轉成json
print("串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型 ", type(jsonData))


