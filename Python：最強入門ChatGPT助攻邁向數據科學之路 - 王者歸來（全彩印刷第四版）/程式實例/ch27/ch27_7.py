# ch27_7.py
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
cities = {'人口數':[10000000,8500000,8000000,15000000,6000000,8000000],
          '面積':[400,500,850,300,200,320],
          'town':['紐約','芝加哥','曼谷','東京',
                   '新加坡','香港']}
tw = pd.DataFrame(cities,columns=['人口數','面積'],index=cities['town'])

fig, ax = plt.subplots()
fig.suptitle("世界城市人口數統計")
ax.set_ylabel("人口數")
ax.set_xlabel("城市")
ax.ticklabel_format(style='plain')      # 不用科學記號表示
ax2 = ax.twinx()
ax2.set_ylabel("面積")
tw['人口數'].plot(ax=ax,rot=90)         # 繪製人口數線
tw['面積'].plot(ax=ax2, style='g-')     # 繪製面積線
ax.legend(loc=1)                        # 圖例位置在右上
ax2.legend(loc=2)                       # 圖例位置在左上
plt.show()








