# ch14_30.py
import zipfile

listZipInfo = zipfile.ZipFile('out29.zip', 'r')
print(listZipInfo.namelist())       # 以列表列出所有壓縮檔案
print("\n")
for info in listZipInfo.infolist():
    print(info.filename, info.file_size, info.compress_size)




