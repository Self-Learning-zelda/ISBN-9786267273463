# ex24_6.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

s = np.random.triangular(-5, 4, 5, 10000)
plt.hist(s, bins=200, density=True)
# 繪製曲線圖
sns.kdeplot(s)
plt.show()









