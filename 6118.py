from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    n1, n2 = map(int, input().split())
    board[n1].append(n2)
    board[n2].append(n1)

def bfs():
    deq = deque()
    deq.append(1)   
    while deq:
        pv = deq.popleft()
        for tv in board[pv]:
            if tv!=1 and visit[tv]==0:
                visit[tv]=visit[pv]+1
                deq.append(tv)
            
bfs()

max_v = max(visit)
idx = visit.index(max_v)
cnt = visit.count(max_v)
print(idx,max_v,cnt)