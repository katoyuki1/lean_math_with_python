import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 6)
y = 1/2 * x + 1/2
y2 = -2 * x + 7

# グラフを描画
plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal') # x軸とy軸の目盛りの増分を等しくする記述。matplotlibはグラフ全体が表示されるよう目盛りの大きさを自動調整するから
plt.grid(color='0.8')
plt.show()