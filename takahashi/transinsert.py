# 交通費精算DB

# import datetime    #モジュールごとのimportする記述
# from datetime import date
import sys
from database import session
from tables import Transports

# 引数の取得
try:
    args = sys.argv
    input_date = int(args[1]) #日付
    input_seq = int(args[2]) #連番
    input_departure = str(args[3]) # 出発地
    input_arrival = str(args[4]) # 到着地
    input_via = str(args[5]) # 経由/利用交通機関
    input_amount = int(args[6]) # 金額

#登録の値を設定
    transport = Transports(
        date = input_date, 
        seq_tra = input_seq, 
        departure = input_departure, 
        arrival = input_arrival,
        via = input_via,
        amount = input_amount
    )
    #INSERT
    session.add(transport)
    #コミット
    session.commit()
    # 結果の出力
    print("交通費精算テーブルにデータを登録しました")
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")



# 連番最大値を取得
# Transportget = session.query(Transports).filter_by(date = input_date).order_by(Transports.seq_tra.desc()).first()

# 結果の出力
# if Transportget != None:
#     print("error:交通費精算テーブルにデータを登録できませんでした")
# else:
#     print("交通費精算テーブルにデータを登録しました")