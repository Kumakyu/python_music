# 素数判定program
# モジュールの取り込み
import sys

# 関数の定義
def Prime(num):
    if num < 2: # 2より小さい数は素数でない
        return False
    i = 2
    while i * i <= num: # 2,3は素数だから4からの判定（2,3に対してはTrueを返す）
        if num % i == 0:
            return False
        i += 1
    return True

# 引数の入力
args = sys.argv
num= int(args[1])

if Prime(num):
        print("Prime", end="")
else:
    if num >= 1000:
        print("1000以上は判定できません", end="")
    else:
        print("not", end="")