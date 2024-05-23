#交通費精算DBを作成するプログラム
from database import session
from transport_table import Transport
import sys
args = sys.argv

#引数の入力
date_input = int(args[1])
seq_input = int(args[2])
departure_input = str(args[3])
arrival_input = str(args[4])
via_input = str(args[5])
amount_input = int(args[6])

#引数をテーブルに挿入
try:
    transport = Transport(
        date = date_input,
        seq = seq_input,
        departure = departure_input,
        arrival = arrival_input,
        via = via_input,
        amount = amount_input
    )
    #INSERT処理
    session.add(transport)
    #コミット
    session.commit()
    print("交通費精算テーブルにデータを登録しました")

#例外処理
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")
