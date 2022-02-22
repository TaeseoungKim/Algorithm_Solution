from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
ntree = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    n1,n2 = map(int, input().split())
    ntree[n1].append(n2)
    ntree[n2].append(n1)

def bfs(v):
    deq = deque()
    visit[v]=1
    deq.append(v)
    while deq:
        pv = deq.pop()
        for n in ntree[pv]:
            if visit[n]==1:
                continue
            parent[n]=pv
            visit[n]=1
            deq.append(n)

for i in range(1,n+1):
    if visit[i]==0:
        bfs(i)
for i in range(2,n+1):
    print(parent[i])