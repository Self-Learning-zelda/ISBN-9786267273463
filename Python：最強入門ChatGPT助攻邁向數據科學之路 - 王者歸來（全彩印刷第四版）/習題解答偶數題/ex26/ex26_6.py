# ex26_6.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
x = pd.read_excel("data26_6.xlsx",skiprows=3,usecols="B:F")
print(x)







