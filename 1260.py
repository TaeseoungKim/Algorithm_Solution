import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
m_list = [ [0] * (n+1) for _ in range(n+1) ]
visit = [0]*(n+1)
for _ in range(m):
    n1, n2 = map(int, input().split())
    m_list[n1][n2] = 1
    m_list[n2][n1] = 1

def dfs(v):
    visit[v]=1
    print(v,end=" ")
    for i in range(1,n+1):
        if visit[i] != 1 and m_list[v][i]==1:
            dfs(i)

bfs_deq = deque()
def bfs(v):
    bfs_deq.append(v)
    visit[v]=1
    while bfs_deq:
        p = bfs_deq.popleft()
        print(p,end=" ")
            
        for i in range(1,n+1):
            if visit[i] != 1 and m_list[p][i]==1:
                bfs_deq.append(i)
                visit[i]=1

dfs(v)
visit = [0]*(n+1)
print()
bfs(v)
