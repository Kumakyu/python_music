from database import session
from tables import Stations
import sys
args = sys.argv
station1 = args[1]
station2 = args[2]

get_kilo1 = session.query(Stations.kilo).filter_by(name = station1).first().kilo
get_kilo2 = session.query(Stations.kilo).filter_by(name = station2).first().kilo

if get_kilo1 > get_kilo2:
   A = get_kilo1 - get_kilo2
   truncated_number_round = round(A, 2)
   print(truncated_number_round, end="")
else:
   A = get_kilo2 - get_kilo1
   truncated_number_round = round(A, 2)
   print(truncated_number_round, end="")