#新幹線の駅間を計算するプログラム
from database import session
from tables import Station
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys
args = sys.argv
 
#引数の入力
st1 = str(args[1])
st2 = str(args[2])

kyori1 = session.query(Station.kilo).filter_by(name = st1).first().kilo
kyori2 = session.query(Station.kilo).filter_by(name = st2).first().kilo

#東京駅からの距離がst1の方がst2よりも近い場合
if kyori1 < kyori2:
    distance = kyori2 - kyori1
#東京駅からの距離がst2の方がst1よりも近い場合
elif kyori1 > kyori2:
    distance = kyori1 - kyori2
#距離の計算
distance = Decimal(str(distance)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
print(distance)
