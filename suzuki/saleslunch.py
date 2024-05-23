from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
kara = int(args[1])
curry = int(args[2])


total = kara*760 + curry*850

cost1 = (kara*760)*0.323
cost2 = (curry*850)*0.284
cost1 = Decimal(str(cost1)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
cost2 = Decimal(str(cost2)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

total_cost = cost1 + cost2

profit = total - total_cost

print("売上高：" + str(total) + "、" + "原価：" + str(total_cost) + "、" + "粗利：" + str(profit), end="")
