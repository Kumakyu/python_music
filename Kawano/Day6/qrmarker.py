#パッケージのインポート
import qrcode

#
with open("../QR/QRtest.txt",encoding="utf-8") as qrf:    
    #QRコード複数作成処理
    for i, line in enumerate(qrf):
        ##QRコードを作成
        URL = line
        img = qrcode.make(URL)
        ##ファイルに保存
        img.save(f"../QR/2-{i+1}.png")