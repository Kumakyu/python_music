# QRコードのプログラム

# モジュールの取り込み
import qrcode
import sys
import os

# 引数の入力
args = sys.argv # url

#qrコードを作成するURL
with open(os.path.join("..","../../files/qrlist.txt"), mode = "w", encoding="utf-8") as f:
    for i in range(1,len(args)):
        f.write(args[i] + "\n")
        img = qrcode.make(args[i])
        img.save(os.path.join("..","../../files", str(i) + ".png")) # 画像の保存（フルパスを作成して保存）