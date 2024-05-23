from database import session
from tables2 import Transport
from datetime import date

datalist = session.query(Transport).all
with open("./output/output.txt", mode="w",encoding="utf-8") as tf:
    for line in datalist(): 
        t2 = line.date
        tf.write('"' + t2.strftime("%Y%m%d") + '"' + "," +'"' + str(line.seq) + '"'+","
            +'"' + line.departure + '"' + "," +'"' + line.arrival + '"' + "," +'"' + line.via + '"' + ","
            +'"' + str(line.amount) + '"\n')

