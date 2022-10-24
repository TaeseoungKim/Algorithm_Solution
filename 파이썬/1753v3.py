import sys
import heapq

input = sys.stdin.readline
INF = 2e9
V, E = map(int, input().split())
s = int(input())  # 시작 정점
board = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    board[u].append((v, w))

dp = [INF for _ in range(V+1)]
dp[s] = 0
for distNode, wei in board[s]:
    dp[distNode] = wei

# 다익스트라
queue = []
heapq.push(queue, (dp[s], s))

while queue:
    curDist, cur_dest = heapq.heappop(queue)

    if dp[dest] > curDist
