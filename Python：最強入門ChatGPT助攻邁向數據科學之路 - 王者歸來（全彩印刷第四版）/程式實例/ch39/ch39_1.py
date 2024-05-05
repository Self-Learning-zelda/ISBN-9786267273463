# ch39_1.py
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# 加載手寫數字數據集
digits = load_digits()
X = digits.data
y = digits.target

# 繪製前 16 張圖像
num_images = 16
rows = 4
cols = 4
fig, axes = plt.subplots(rows, cols, figsize=(10, 10))

for i in range(rows):
    for j in range(cols):
        index = i * cols + j
        # 將 64 維向量重塑為 8x8 的圖像
        img = X[index].reshape(8, 8)       
        axes[i, j].imshow(img, cmap='gray')
        axes[i, j].set_title(f'Label: {y[index]}')
        axes[i, j].axis('off')

plt.show()




