#引数がマイナスの時の処理まで欲しい
#引数設定
import sys
args = sys.argv
distance = int(args[1])
THRESHOLD = 1500
DISTANCE_UPPER_THRESHOLD = 344
FEE_UNDER_THRESHOLD = 630
FEE_UPPER_THRESHOLD = 98

#処理　
if distance <= THRESHOLD:##1500m以下のとき
    fee = int(FEE_UNDER_THRESHOLD)
else: ##1500m以上のとき
    surplus_distance = distance - THRESHOLD ###1500m以上の距離
    if surplus_distance % DISTANCE_UPPER_THRESHOLD == 0:
        surplus_surplus_distance = surplus_distance % DISTANCE_UPPER_THRESHOLD ###1500m以上分を344mで割ったあまり
        count_increase_times = ((surplus_distance - surplus_surplus_distance) / DISTANCE_UPPER_THRESHOLD)   ###344mの回数
    else:
        surplus_surplus_distance = surplus_distance % DISTANCE_UPPER_THRESHOLD ###1500m以上分を344mで割ったあまり
        count_increase_times = ((surplus_distance - surplus_surplus_distance) / DISTANCE_UPPER_THRESHOLD) + 1  ###344mの回数
    fee = FEE_UNDER_THRESHOLD + count_increase_times*FEE_UPPER_THRESHOLD
    fee = int(fee)
#出力
print(fee, end="")