import qrcode

a_file = open("qr_url.txt", encoding="utf-8")
url = a_file.readlines()

for i in url:
#QRコード作成
    img = qrcode.make(i)
    img.save("/home/matcha-23training/projects/python/files/", {0}.png.format(i))

#ファイル閉じる
a_file.close()

#ファイルの読み込み一行ずつにする
#一行ずつQRコード作成
#