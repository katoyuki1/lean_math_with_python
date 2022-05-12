import matplotlib.pyplot as plt
import numpy as np

# 角度 0〜359の角度を配列で取得
th = np.arange(0, 360)

# 円周上の点Pの座標、radians関数は弧度法の値に変換する処理
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))
"""
点(2,3)を中心にした円にしたい場合
x = np.cos(np.radians(th)) + 2
y = np.sin(np.radians(th)) + 3
"""

"""
# 半径が１以外の円を描画する場合
r = 5 # 円の半径
x = r * np.cos(np.radians(th))
y = r * np.sin(np.radians(th))
"""

# 描画
plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()