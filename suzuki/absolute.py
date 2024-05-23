import sys
args = sys.argv
number = int(args[1])

if number >= 0:
    ab = number - (2*number)
else:
    ab = (number) + (-2*number)

print(str(number) + " " + str(ab) , end="")

