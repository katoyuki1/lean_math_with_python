import matplotlib.pyplot as plt

# データ
x = list(range(1, 11)) # xの値（１〜１０）
y = []
for i in range(10):
    y.append(3 * x[i] -24) # y = 3x - 24

# グラフ
plt.plot(x, y, marker='o')
plt.grid(color='0.8')
plt.show()