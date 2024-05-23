#タクシー運賃を計算するプログラム

import math
import sys
args = sys.argv

distance = int(args[1])
#運賃の計算
if distance <= 1500: #距離が1500ｍ以下
    fare = 630
elif distance > 1500: #距離1500ｍ～
    add_distance = distance - 1500 #1500ｍ走行後、何ｍ走行しているか
    add_fare = ((math.ceil(add_distance / 344))) * 98 #追加運賃の計算
    fare = 630 + add_fare

print(fare,end="")