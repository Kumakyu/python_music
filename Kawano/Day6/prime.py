#引数設定
import sys
args = sys.argv
num = int(args[1])
prime_count = 0

if num >= 1000:
    print("1000以上は判定できません",end="")
    sys.exit()

##素数の処理
for i in range(2,num+1):
    if num % i == 0:
        prime_count += 1
#出力
if prime_count > 1:
    print("not",end="")
else:print("Prime",end="")

