n = int(input())
Fibonacci  = [1,1]
for i in range(2,n+1):
    Fibonacci.append(Fibonacci[i-2] + Fibonacci[i-1])

print(Fibonacci[n] % 10007)