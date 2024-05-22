#ランチの粗利を計算するプログラム

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys
args = sys.argv

#引数の入力
karaage = int(args[1])
curry = int(args[2])

#１日の売上高の計算
karaage_sales = 760 * karaage
curry_sales = 850 * curry
#原価＝売上高×原価率　→　少数第一位を四捨五入し整数値で原価算出
karaage_cost = Decimal(karaage_sales * 0.323).quantize(Decimal('0'), ROUND_HALF_UP)
curry_cost = Decimal(curry_sales * 0.284).quantize(Decimal('0'), ROUND_HALF_UP)
#粗利＝売上高ー原価
karaage_arari = karaage_sales - karaage_cost
curry_arari = curry_sales - curry_cost

#メニューごとに整数値を出し、合計値（売上高、原価、粗利）を得る
sales_sum = karaage_sales + curry_sales
cost_sum = karaage_cost + curry_cost
arari_sum = karaage_arari + curry_arari

print("売上高：{0}、原価：{1}、粗利：{2}".format(sales_sum, cost_sum, arari_sum),end="")