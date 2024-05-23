from datetime import date
from database import session
from tables2 import Transport
import sys
args =sys.argv
in_date = args[1]
in_seq = int(args[2])
in_departure =args[3]
in_arrival = args[4]
in_via = args[5]
in_amount = int(args[6])

# 登録するデータの編集
try:
    transport= Transport(
        date = date(int(in_date[0:4]),int(in_date[4:6]),int(in_date[6:8])),
        seq = in_seq,
        departure = in_departure,
        arrival = in_arrival,
        via = in_via,
        amount = in_amount
    )
    #INSERT処理
    session.add(transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました")
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")