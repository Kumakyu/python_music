# 交通費精算を一覧で出力するプログラム

#モジュールごとのimportする記述
from datetime import date
import sys, os, qrcode
from database import session
from tables import Transports

# 引数の入力
args = sys.argv
file_name = str(args[1])

# SELECT（全件取得）
translist = session.query(Transports).all()

# 書き込む
with open(os.path.join("..","../../files", file_name), mode = "w", encoding="utf-8") as f:
    for trans in translist:
        f.write(
            '"'+str(trans.date)+'"' + "," + '"'+str(trans.seq_tra)+'"' + "," 
            + '"'+trans.departure+'"' + "," + '"'+trans.arrival+'"'
            + '"'+trans.via+'"' + "," + '"'+str(trans.amount)+'"' + "\n")
        