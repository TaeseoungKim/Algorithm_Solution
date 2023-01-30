import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
edges = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    edges[x-1][y-1] = True
    edges[y-1][x-1] = True


def dfs(N, edges, V):  # 깊이우선
    visited = [False for i in range(N)]
    queue = deque()
    queue.append(V-1)
    answer = []

    while queue:
        pNode = queue.pop()
        if visited[pNode]:
            continue
        visited[pNode] = True
        answer.append(pNode+1)
        for i in range(N-1, -1, -1):
            if i == pNode or visited[i]:
                continue
            if edges[pNode][i]:
                queue.append(i)
    print(*answer)


def bfs(N, edges, V):  # 너비우선
    visited = [False for i in range(N)]
    visited[V-1] = True
    queue = deque()
    queue.append(V-1)
    answer = []

    while queue:
        pNode = queue.popleft()
        answer.append(pNode+1)
        for i in range(N):
            if i == pNode or visited[i]:
                continue
            if edges[pNode][i]:
                visited[i] = True
                queue.append(i)
    print(*answer)


dfs(N, edges, V)
bfs(N, edges, V)
