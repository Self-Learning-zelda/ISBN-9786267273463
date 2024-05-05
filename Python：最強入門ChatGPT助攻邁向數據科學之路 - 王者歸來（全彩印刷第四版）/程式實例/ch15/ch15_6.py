# ch15_6.py

fn = 'data15_6.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    wordList = data.split()     # 將文章轉成串列
    print(f"{fn} 文章的字數是 {len(wordList)}")    # 列印文章字數





