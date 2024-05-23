#引数設定
import sys
args = sys.argv
count_karaage = int(args[1])
count_currey = int(args[2])
PRICE_KARAAGE = 760
PRICE_CURREY = 850

#処理
sales_total = int(count_karaage*PRICE_KARAAGE + count_currey*PRICE_CURREY)

#出力
print(sales_total,end="")