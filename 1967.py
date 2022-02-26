from collections import deque
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
#https://kyun2da.github.io/2021/05/04/tree's_diameter/
n = int(input())
board = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y,w = map(int, input().split())
    board[x].append([y,w])
    board[y].append([x,w])

def dfs(v,wei):
    visit[v]=1
    dist.append((wei,v))

    for tmp_v,tmp_wei in board[v]:
        if visit[tmp_v]==0:
            dfs(tmp_v,wei+tmp_wei)
    
dist = []
visit = [0]*(n+1)
dfs(1,0)
max_Value = max(dist)
max_Index = dist[dist.index(max_Value)][1]

dist = []
visit = [0]*(n+1)
dfs(max_Index,0)
print(max(dist)[0])
