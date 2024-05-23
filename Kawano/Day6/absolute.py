#引数の出力
import sys
args = sys.argv
num = int(args[1])

#絶対値処理
num_abs = abs(num)

#出力
print(f"{num} {num_abs}",end="")