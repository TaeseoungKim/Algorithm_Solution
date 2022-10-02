import sys
import heapq
input = sys.stdin.readline
n = int(input())
board = []
heap = []

answ=0
for _ in range(n):
    board.append(list(map(int, input().split())))
board.sort(key=lambda x: x[1])

for i in range(n):
    heapq.heappush(heap, board[i])
    if len(heap)>board[i][1]:
        heapq.heappop(heap)

for i in range(len(heap)):
    answ+=heapq.heappop(heap)[0]
print(answ)