import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    n1, n2 = map(int, input().split())
    edges[n1][n2] = 1
    edges[n2][n1] = 1

cnt = 0
def bfs(v):
    deq = deque()
    global cnt
    cnt += 1
    visit[v] = 1
    deq.append(v)
    while deq:
        dv = deq.pop()
        for i in range(1,n+1):
            if visit[i]==0 and edges[dv][i]==1:
                visit[i]=1
                deq.append(i)
                
    

for i in range(1,n+1):
    if visit[i]==0:
        bfs(i)
print(cnt)