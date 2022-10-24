import sys
from collections import deque

input = sys.stdin.readline
INF = 2e9
V, E = map(int, input().split())
s = int(input())  # 시작 정점
board = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    board[u].append((v, w))

dp = [INF for _ in range(V+1)]

for distNode, wei in board[s]:
    dp[distNode] = wei

# 1: 0
# 2: 2
# 3: 1
# 4: 3


def bfs(cur):
    queue = deque()
    queue.append(cur)
    visited[cur] = True
    dp[cur] = 0

    while queue:
        curNode = queue.popleft()
        for nextNode, wei in board[curNode]:
            if dp[nextNode] > dp[curNode]+wei or visited[nextNode] == False:
                visited[nextNode] = True
                queue.append(nextNode)
                dp[nextNode] = min(dp[curNode]+wei, dp[nextNode])


bfs(s)
print("정답")
for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
