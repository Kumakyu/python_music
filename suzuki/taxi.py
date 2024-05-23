import sys
args = sys.argv
dis = int(args[1])

if dis <= 1500:
    money = 630
else:
    count = -(-(dis - 1500)//344)
    money = 630 + 98*count
print(str(money), end="")