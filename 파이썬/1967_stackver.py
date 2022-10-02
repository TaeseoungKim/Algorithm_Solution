from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
board = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y,w = map(int, input().split())
    board[x].append([y,w])
    board[y].append([x,w])

def dfs(v,wei):
    deq = deque()
    deq.append((v,wei))
    while deq:
        pop_v, pop_wei = deq.pop()
        visit[pop_v]=1
        dist.append((pop_wei,pop_v))
        for tmp_v,tmp_wei in board[pop_v]:
            if visit[tmp_v]==0:
                deq.append((tmp_v,pop_wei+tmp_wei))

dist = []
visit = [0]*(n+1)
dfs(1,0)
max_Value = max(dist)
max_Index = dist[dist.index(max_Value)][1]

dist = []
visit = [0]*(n+1)
dfs(max_Index,0)
print(max(dist)[0])
