from database import session # 1.データベースへの接続
from tables import Stations # 2.テーブル定義

# 登録するデータの編集
# 追加する駅のデータを辞書のリストで定義
stations_data =[
    {"seq":1, "name":"東京", "kilo":0.00},
    {"seq":2, "name":"品川", "kilo":6.78},
    {"seq":3, "name":"新横浜", "kilo":25.54},
    {"seq":4, "name":"名古屋", "kilo":342.02},
    {"seq":5, "name":"京都", "kilo":476.31},
    {"seq":6, "name":"新大阪", "kilo":515.35}
]

# リスト内の各データに対してStationを作成し、データベースに追加
for station_data in stations_data:
    station = Stations(**station_data)
    session.add(station) # INSERT処理

# コミット
session.commit()