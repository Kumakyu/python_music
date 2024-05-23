#ランチの売り上げを計算するプログラム

import sys
args = sys.argv

#引数の入力
karaage = int(args[1])
curry = int(args[2])

#売上の計算
sales = 760 * karaage + 850 * curry
print(sales,end="")