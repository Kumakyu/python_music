#引数が整数か素数かを判断するプログラム
import sys
args = sys.argv
 
#引数の入力
num = int(args[1])
count = 0 

#1000以上の場合判定しない
if num >= 1000:
    print("1000以上は判定できません",end="")
 
else:
    for i in range(2,num-1):
        amari = num % i
        if amari == 0:
            count = count + 1
            break

    if count != 0:
        print("not",end="")
    elif count == 0:
        print("Prime",end="")
