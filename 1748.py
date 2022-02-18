import sys,math
input = sys.stdin.readline
n = int(input())

result = 0
dig = int(math.log10(n))+1

if n < 10:
    print(n)
else:
    for _ in range(dig-1):
        result += 9*(10**_)*(_+1)
    rem = n-10**(dig-1) + 1
    result += rem*(dig)
    
    print(result)
