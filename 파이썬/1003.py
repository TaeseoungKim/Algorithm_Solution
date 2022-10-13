import sys
input = sys.stdin.readline


zero = 0
one = 0

fiboDic = {0: [0, 1, 0], 1: [1, 0, 1], 2: [1, 1, 1], 3: [2, 1, 2]}


def fibonacci(n):
    global zero, one
    if n in fiboDic:
        return fiboDic[n]

    if n == 0:
        zero += 1
        return 0, zero, one
    elif n == 1:
        one += 1
        return 1, zero, one
    else:
        temp1 = fibonacci(n-1)
        temp2 = fibonacci(n-2)
        fiboDic[n] = [temp1[0]+temp2[0], temp1[1]+temp2[1], temp1[2]+temp2[2]]
        return fiboDic[n]


T = int(input())
for _ in range(T):
    N = int(input())
    fibonacci(N)
    print(fiboDic[N][1], fiboDic[N][2])
