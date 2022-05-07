import matplotlib.pyplot as plt
import numpy as np # Numpy. 数値計算用のライブラリ

x = np.arange(-1.0, 1.01, 0.01) # x軸の値を代入する処理
y = x ** 2 # y軸の値, 二次関数（quadratic function）
"""
↓リストにしたければ
y = []
for i in range(len(x)):
    y.append(x[i] ** 2)
"""

# グラフを描画
plt.plot(x, y)
plt.grid(color='0.8')
plt.show()