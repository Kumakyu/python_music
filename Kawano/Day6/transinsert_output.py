from datetime import date
#import datetime    #モジュールごとのimportする記述
import sys
#mysqlDB接続、テーブル
from transinsert_database import session
from transinsert_tables import Transport
#DBから各レコードの取得
max_seq = max(session.query(Transport.seq)).seq
print(max_seq)
with open("transport.txt", mode="w", encoding="utf-8") as f:
        
    for i in range(1,max_seq+1):
        get_date = session.query(Transport.date).filter_by(seq = i).first().date
        get_seq  = session.query(Transport.seq).filter_by(seq = i).first().seq
        get_depature  = session.query(Transport.depature).filter_by(seq = i).first().depature
        get_arrival  = session.query(Transport.arrival).filter_by(seq = i).first().arrival
        get_via  = session.query(Transport.via).filter_by(seq = i).first().via
        get_amount  = session.query(Transport.amount).filter_by(seq = i).first().amount
        f.write(f'"{get_date}","{get_seq}","{get_depature}","{get_arrival}","{get_via}","{get_amount}"\n')


