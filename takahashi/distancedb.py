# 新幹線の駅間を計算するプログラム
from database import session # 1.データベースへの接続
from tables import Stations # 2.テーブル定義

# モジュールの取り込み
import sys
args = sys.argv

# 引数の入力
station1 = str(args[1])
station2 = str(args[2])

# データのSELECT
departure = session.query(Stations.kilo).filter_by(name = station1).first().kilo # 出発駅のデータをSELECT
arrival = session.query(Stations.kilo).filter_by(name = station2).first().kilo # 到着駅のデータをSELECT

distance = abs(departure - arrival) # 距離の計算

# 結果の出力
print(distance)