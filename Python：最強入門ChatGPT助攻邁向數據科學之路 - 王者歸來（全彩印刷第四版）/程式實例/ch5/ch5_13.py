# ch5_13.py
print("判斷輸入年份是否閏年")
year = input("請輸入年份: ")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print(f"{year} 是閏年")
    else:
        print(f"{year} 不是閏年")
else:
    print(f"{year} 不是閏年")
