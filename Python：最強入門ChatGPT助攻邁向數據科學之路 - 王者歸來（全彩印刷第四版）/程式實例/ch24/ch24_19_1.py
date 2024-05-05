# ch24_19_1.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

s = np.random.triangular(-2, 0, 10, 10000)
plt.hist(s, bins=200, density=True)
# 繪製曲線圖
sns.kdeplot(s)
plt.show()









