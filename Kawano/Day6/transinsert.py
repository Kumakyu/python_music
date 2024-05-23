#インポートの設定
import sys
from datetime import date
from transinsert_database import session
from transinsert_tables import Transport
#引数の設定
args = sys.argv
input_date = args[1]
input_date = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
input_seq = int(args[2])
input_depature = str(args[3])
input_arrival = str(args[4])
input_via = str(args[5])
input_amount = int(args[6]) 
try:
    # 登録するデータの編集
    transport= Transport(
        date = input_date ,
        seq = input_seq ,
        depature = input_depature ,
        arrival = input_arrival ,
        via = input_via ,
        amount = input_amount
    )
    #INSERT処理
    session.add(transport)
    #コミット
    session.commit()
    print("交通費生産テーブルにデータを登録しました")
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")