from sympy import Symbol, solve # SympyからSymbolクラスとsolve関数をインポート

# 計算式の中で使う文字の定義
a = Symbol('a')
b = Symbol('b')
# 連立方程式で使う式を定義
ex1 = a + b - 1
ex2 = 5*a + b - 3

# 連立方程式を解く
print(solve((ex1, ex2))) # 二つの式をタプルにしてsolveに渡すと解が求まる