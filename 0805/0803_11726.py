# 항상 문제를 풀 때, 경우의 수 마다 어떤 규칙이 있는지 찾자.
# n = 0 => 1
# n = 1 => 1
# n = 2 => 2
# n = 3 => 3
# n = 4 => 5
# n = 5 => 8
# 피보나치 재귀함수를 사용했더니 시간초과가 난다.

n = int(input())
Fibonacci  = [1,1]
for i in range(2,n+1):
    Fibonacci.append(Fibonacci[i-2] + Fibonacci[i-1])

print(Fibonacci[n] % 10007)



# def Fibonacci(n):
#     if n == 1 or n == 2 or n == 3:
#         return n # early return
#     sum = Fibonacci(n-1) + Fibonacci(n-2)
#     return sum
# print(Fibonacci(n))