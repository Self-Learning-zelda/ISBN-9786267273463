# ch27_3.py
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
cities = {'人口數':[1000, 850, 800, 1500, 600, 800],
          'town':['紐約','芝加哥','曼谷','東京',
                   '新加坡','香港']}
tw = pd.DataFrame(cities,columns=['人口數'],index=cities['town'])
          
tw.plot(title='世界城市人口數統計',kind='bar')
plt.xlabel("城市")
plt.ylabel("人口數")
plt.show()








