from distancedb_database import session
from distancedb_table import Stations

datalist = [[1,"東京",0.00],[2,"品川",6.78],[3,"新横浜",25.54],[4,"名古屋",342.02],[5,"京都",476.31],[6,"新大阪",515.35]]
for i in range(len(datalist)):
    # 登録するデータの編集
    stations= Stations(
        seq = datalist[i][0] ,
        name = datalist[i][1] ,
        kilo = datalist[i][2]
    )
    #INSERT処理
    session.add(stations)
    #コミット
    session.commit()