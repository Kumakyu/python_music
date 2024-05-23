import qrcode
i=0
with open("qrlist.txt", encoding="utf-8") as tf:
    for line in tf:
        i+=1
        img = qrcode.make(line)
        img.save("./output/" + str(i) + ".png")