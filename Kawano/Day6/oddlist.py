#初期設定
list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
oddlist = []
#処理
for i in list[1::2]:
    oddlist.append(i)
print(oddlist)
