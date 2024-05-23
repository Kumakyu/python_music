#QRコードを大量作成するプログラム
import qrcode

#ファイルを開く
a_file = open("qr_url.txt", encoding="utf-8")

#ファイルを読み込む
line = []

textlist = a_file.readline() #一行目のURL読み込み
img = qrcode.make(textlist) #QRコード作成
filename = "sample.png"
img.save("/home/matcha-23training/projects/python/files/", filename)
#QRコードに出力
# for i in line:
#     textlist = a_file.readline() #一行目のURL読み込み
#     line.append(textlist)
#     print(str(i))
#     img = qrcode.make(i) #QRコード作成
#     filename = (str(i+1) + ".png")
#     img.save("/home/matcha-23training/projects/python/files/", filename) #QRコード保存
#     textlist = a_file.readline() #次の行のURL読み込み
a_file.close()
