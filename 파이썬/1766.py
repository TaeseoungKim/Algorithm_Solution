import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
heapQueue = []

board = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    board[A].append(B)
    degree[B] += 1

for i in range(1,N+1):
    board[i].sort()
    if degree[i]==0:
        heapq.heappush(heapQueue, i)

answer = []
while heapQueue:
    pNode = heapq.heappop(heapQueue)
    answer.append(pNode)
    for nextNode in board[pNode]:
        degree[nextNode] -= 1
        if degree[nextNode] == 0:
            heapq.heappush(heapQueue,nextNode)

print(*answer)