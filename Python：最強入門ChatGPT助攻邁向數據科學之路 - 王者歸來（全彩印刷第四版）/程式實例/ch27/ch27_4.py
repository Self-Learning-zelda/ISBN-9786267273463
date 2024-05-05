# ch27_4.py
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
cities = {'人口數':[1000, 850, 800, 1500, 600, 800],
          '面積':[400,500,850,300,200,320],
          'town':['紐約','芝加哥','曼谷','東京',
                   '新加坡','香港']}
tw = pd.DataFrame(cities,columns=['人口數','面積'],index=cities['town'])
          
tw.plot(title='世界城市人口數統計')
plt.xlabel("城市")
plt.show()








