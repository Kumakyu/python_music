# タクシーの運賃を計算するプログラム

# モジュールの取り込み
import sys
args = sys.argv

distance = int(args[1]) # 引数の入力
taxi_fee = 0 # 運賃の初期化

# 運賃の計算
if distance <= 1500: # 1500mまでは630円
    taxi_fee = 630 # 料金の計算
else:
    count = 1 + int((distance - 1500) / 344) # 98円を足す回数
    taxi_fee = 630 + 98 * count # 料金の計算

# 結果の出力
print(taxi_fee, end="")