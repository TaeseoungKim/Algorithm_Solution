from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for d in range(i+1,n):
        if board[i]<board[d]:
            dp[d] = max(dp[d],dp[i]+1)
max_V = max(dp)
print(max_V)
max_Idx = dp.index(max_V)
deq = deque()
for i in range(max_Idx,-1,-1):
    if max_V == dp[i]:
        deq.appendleft(board[i])
        max_V -= 1        
print(*deq)
