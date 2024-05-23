import sys
args = sys.argv
number = int(args[1])

if number >= 1000:
    print(str(1000) + "以上は判定できません", end="")
elif number < 2:
    print("not", end="")
else:

    for i in range(2,number):
        if number % i == 0:
            print("not", end="")
            sys.exit()

    print("Prime", end="")

