import sys
input = sys.stdin.readline

n = int(input())
board = []
dp = [0]*(n+1)
for _ in range(n):
    board.append(list(map(int, input().split())))

#M에 현재까지 벌어들인 최대 수익을 갱신해주는게 문제의 핵심!!
M=0
for i in range(n):
    next = i+board[i][0]
    M = max(M,dp[i])
    if next>n: continue
    dp[next]=max(dp[next],M+board[i][1])
print(max(dp))