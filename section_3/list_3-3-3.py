import matplotlib.pyplot as plt
import numpy as np # Numpy. 数値計算用のライブラリ

x = np.arange(-1.0, 1.01, 0.01) # x軸の値を代入する処理
y = x ** 3 - x # y軸の値, 三次関数（Cubic function）
"""
↓リストにしたければ
y = []
for i in range(len(x)):
    y.append(x[i] ** 3 - x)
"""

# グラフを描画
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()