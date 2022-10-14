import sys
input = sys.stdin.readline

N = int(input())
board = [0]
for i in list(map(int, input().split(" "))):
    board.append(i)
dp = [-1 for i in range(N+1)]


def dpSol(num, div):

    quotient = num//div
    remainder = num % div

    if remainder == 0:
        dp[num] = max(dp[num], dp[div]*quotient)
    else:
        dp[num] = max(dp[num], dp[quotient*div]+dp[remainder])


for i in range(1, N+1):
    for d in range(1, i+1):
        if i == d:
            dp[i] = max(dp[i], board[i])
            continue
        dpSol(i, d)

print(dp[N])
