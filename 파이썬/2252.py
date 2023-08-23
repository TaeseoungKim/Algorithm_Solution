import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [[] for i in range(N+1)]
degree = [0 for i in range(N+1)]
deq = deque()
for i in range(M):
    X, Y = map(int, input().split())
    board[X].append(Y)
    degree[Y] += 1

for i in range(1,N+1):
    if degree[i]==0:
        deq.append(i)
result = []
while deq:
    pNode = deq.popleft()
    result.append(pNode)

    for i in range(len(board[pNode])):
        degree[board[pNode][i]] -= 1
        if  degree[board[pNode][i]] == 0:
            deq.append(board[pNode][i]) 

print(*result)