# ch20_40.py
import matplotlib.pyplot as plt
from pylab import mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
sorts = ["交通","娛樂","教育","餐費","雜支"]
fee = [8000,2000,3000,5000,6000]
          
plt.pie(fee,labels=sorts,explode=(0,0.2,0,0,0),
        autopct="%1.2f%%")      # 繪製圓餅圖
plt.show()

