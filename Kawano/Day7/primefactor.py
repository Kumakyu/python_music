#引数の設定_Setting argument
import sys
args = sys.argv
num = int(args[1])
i = 2
prime = []
#素因数分解の処理_Processing of prime factorization
while num != 1:
    while num % i == 0:
        num = int(num / i)
        prime.append(i)
    i += 1

#出力_Output
print(prime)



