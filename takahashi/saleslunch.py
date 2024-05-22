# ランチの売り上げを計算するプログラム

# モジュールの取り込み
import sys,math
args = sys.argv

# 引数の入力
order_kara = int(args[1])
order_curry = int(args[2])

# 売上高の計算
sales = 760 * order_kara + 850 * order_curry

# 結果の表示
print(sales, end="")