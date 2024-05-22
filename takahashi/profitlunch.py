# ランチの粗利を計算するプログラム

# モジュールの取り込み
import sys # 引数
from decimal import Decimal, ROUND_HALF_UP # 四捨五入
args = sys.argv

# 引数の入力
order_kara = int(args[1]) # 唐揚げ定食の個数
order_curry = int(args[2]) # カレーセットの個数

# リストの定義
lunch_menu = [{'Name':"kara", 'Price':760, 'Rate':0.323, 'Count':order_kara},
               {'Name':"curry", 'Price':850, 'Rate':0.284, 'Count':order_curry}]

# 初期値の設定
total_sales = 0
total_cost = 0
total_profit = 0

# 繰り返しの処理
for item in lunch_menu:
    sales = item['Price'] * item['Count'] # 売上高
    cost = sales * item['Rate'] # 原価率をかける
    cost_round = Decimal(str(cost)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) # 四捨五入
    profit = sales - cost_round # 粗利
    total_sales += sales
    total_cost += cost_round
    total_profit += profit 

# 結果の表示
print("売上高：" + str(total_sales) + "、原価：" + str(total_cost) + "、粗利：" + str(total_profit), end="")