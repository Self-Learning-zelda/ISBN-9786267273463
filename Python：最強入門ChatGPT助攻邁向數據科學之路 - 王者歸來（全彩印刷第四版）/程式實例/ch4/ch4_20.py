# ch4_20.py
fobj1 = open("out4_20w.txt", mode="w")   # 取代先前資料
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close( )
fobj2 = open("out4_20a.txt", mode="a")   # 附加資料後面
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close( )



