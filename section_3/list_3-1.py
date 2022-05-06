"""
ローカルで試す方法
1. Anaconddaをインストール
https://www.anaconda.com/products/distribution

2. VSCodeでTerminal > NewTerminalでターミナルを開く
3. list_3-1.pyがあるディクレトリに移動
cd section_3
4. 以下コマンドで実行
python3 list_3-1.py
"""
import matplotlib.pyplot as plt

# データ
x = [1,2,3,4,5,6,7]
y = [64.3, 63.8, 63.6, 64.0, 63.5, 63.2, 63.1]

# グラフを描画

# plt.plot(x, y) #折れ線を描画
#plt.plot(x, y, marker='o') # 折線に点を描画したかったら
# plt.plot(x, y, color='red') # 折線の色を指定
plt.plot(x, y, color='red', marker='o') # 折線に点を描画, 色を指定

plt.grid(color='0.8') # グリッドを表示, 数値一つだけでモノクロ濃度指定となる。
plt.show() # 画面に表示