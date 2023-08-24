import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
deq = deque()

board = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    board[A].append(B)
    degree[B] += 1

for i in range(1,N+1):
    board[i].sort()
    if degree[i]==0:
        deq.append(i)

answer = []
while deq:
    if not (min(deq) == deq[0]):
        tempList = list(deq)
        deq = deque(sorted(tempList) )
    pNode = deq.popleft()
    answer.append(pNode)
    for nextNode in board[pNode]:
        degree[nextNode] -= 1
        if degree[nextNode] == 0:
            deq.appendleft(nextNode)

print(*answer)