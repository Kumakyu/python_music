import qrcode
import sys
args =sys.argv

for i in range(1,len(args)):
    url = args[i]
    img = qrcode.make(url)
    img.save("./output/" + str(i) + ".png")

