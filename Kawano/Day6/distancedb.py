import sys
#mysqlDB接続、テーブル
from distancedb_database import session
from distancedb_table import Stations

args = sys.argv

#引数を変数に代入
station_from = args[1]
station_to = args[2]

#第一引数と第二引数の駅の距離をDBからとってくる
distance_from = session.query(Stations.kilo).filter_by(name = station_from).first().kilo
distance_to = session.query(Stations.kilo).filter_by(name = station_to).first().kilo

#駅間の計算
sta_dis = distance_to - distance_from

#絶対値
sta_dis = abs(sta_dis)

#出力（小数第二位まで出力）
print("{:.2f}".format(sta_dis), end="")
