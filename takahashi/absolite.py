# 絶対値を出力するプログラム

# モジュールの取り込み
import sys
args = sys.argv

num = int(args[1]) # 引数の入力（整数）
ab_num = abs(num) # 絶対値の計算

print(str(num) + " " + str(ab_num), end="")

