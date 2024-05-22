#絶対値の計算を行うプログラム

import sys
args = sys.argv

num = int(args[1])

if num > 0:
    absolute = num
else:
    absolute = num * -1

print(num , absolute,end="")