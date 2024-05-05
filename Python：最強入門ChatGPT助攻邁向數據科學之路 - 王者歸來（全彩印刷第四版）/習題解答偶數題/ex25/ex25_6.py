# ex25_6.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(x, y):                                # 左邊曲面函數
    return (x**2 - y**2)
def animate(i):
    ax[1].view_init(60,i)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,subplot_kw={'projection':'3d'})
# 左邊子圖
ax[0].plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖

# 右邊動畫子圖
ax[1].plot_surface(X, Y, f(X,Y), cmap='hsv')   
ax[1].set_axis_off()                        # 關閉顯示軸
ani = FuncAnimation(fig,func=animate,frames=np.arange(0,360,3),
                    interval=60)
ani.save('my3D.gif',writer='pillow')        # 儲存gif檔案
ax[1].set_title("3D動畫圖")
plt.show()


      
