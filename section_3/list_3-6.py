import matplotlib.pyplot as plt
import numpy as np

# 基となる線分の傾きと切片
a1 = (5-1)/(6-0)
b1 = 1

# 線分の中点
cx = (0 + 6) / 2
cy = (1 + 5) /2

# 線分に直行する直線の傾き（a2 = -1/a1）
a2 = -1 / a1

# 線分に直行する直線の切片（b2 = y - a2*x）
b2 = cy - a2*cx

# 直線の式
x = np.arange(0, 7) # x の値
y1 = a1*x + b1 # もとの直線
y2 = a2*x + b2 # 垂直二等分線

# 描画
plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()