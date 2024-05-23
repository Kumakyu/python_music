#引数設定
import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP
#初期設定
count_karaage = int(args[1]) ##唐揚げの注文数
count_currey = int(args[2]) ##カレーの注文数
PRICE_KARAAGE = 760 ##唐揚げの値段
PRICE_CURREY = 850 ##カレーの値段
COST_RATE_KARAAGE = 0.323 ##唐揚げの原価率
COST_RATE_CURREY = 0.284 ##カレーの原価率
#処理
##売上高の計算
sales_karaage = count_karaage*PRICE_KARAAGE
sales_currey = count_currey*PRICE_CURREY
sales = sales_karaage + sales_currey
##原価の計算
prime_cost_karaage = sales_karaage*COST_RATE_KARAAGE
prime_cost_currey = sales_currey*COST_RATE_CURREY
###整数値表示
prime_cost_karaage = Decimal(str(prime_cost_karaage)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
prime_cost_currey = Decimal(str(prime_cost_currey)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
prime_cost = prime_cost_karaage + prime_cost_currey
##粗利の計算
gross_profit_karaage = sales_karaage - prime_cost_karaage
gross_profit_currey = sales_currey - prime_cost_currey
gross_profit = gross_profit_karaage + gross_profit_currey
#出力
print(f"売上高：{sales}、原価：{prime_cost}、粗利：{gross_profit}",end="")
