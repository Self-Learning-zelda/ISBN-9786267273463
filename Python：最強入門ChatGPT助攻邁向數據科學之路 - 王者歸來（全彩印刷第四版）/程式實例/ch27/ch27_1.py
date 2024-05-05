# ch27_1.py
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
population = [860, 1100, 1450, 1800, 2020, 2200, 2260]
tw = pd.Series(population, index=range(1950, 2011, 10))
tw.plot(title='台灣人口統計')
plt.xlabel("年度")
plt.ylabel("人口數")
plt.show()








