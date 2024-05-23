from distancedb_database import session
from distancedb_table import Stations

# データを取得する
stationslist = session.query(Stations).all()

for stations in stationslist:
    print(stations.seq,stations.name,stations.kilo)