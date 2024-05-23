#交通費精算をファイル出力するプログラム
from database import session
from transport_table import Transport

translist = session.query(Transport).all()
a_file = open("/home/matcha-23training/projects/python/files/translist.txt", mode="w", encoding="utf-8")

#DBのデータをファイルに出力
for i in translist:
    a_file.write("\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\"\n".format(i.date, i.seq, i.departure, i.arrival, i.via, i.amount))
a_file.close()
    #print(i.date)
    #print("\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\"".format(i.date, i.seq, i.departure, i.arrival, i.via, i.amount))