# ch22_11.py
import csv

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)     # 讀取文件下一列
print(headerRow)

