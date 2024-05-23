#引数の出力_Setting arguments
import sys
args = sys.argv
num = int(args[1])

#絶対値処理_Convert absolute value
num_abs = abs(num)

#出力_output result
print(f"{num} {num_abs}",end="")