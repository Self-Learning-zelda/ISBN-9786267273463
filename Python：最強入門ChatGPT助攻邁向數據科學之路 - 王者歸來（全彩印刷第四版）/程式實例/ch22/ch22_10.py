# ch22_10.py
import csv

# 定義串列,元素是字典
dictList = [{'姓名':'Hung','年齡':'35','城市':'台北'},  
          {'姓名':'James', '年齡':'40', '城市':'芝加哥'}]
          
fn = 'out22_10.csv'
with open(fn, 'w', newline = '', encoding = 'utf-8') as csvFile:  
    fields = ['姓名', '年齡', '城市']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件
    dictWriter.writeheader()                                # 寫入標題
    for row in dictList:                                    # 寫入內容
        dictWriter.writerow(row)




