import queue
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
navi = [ [] for _ in range(N) ]
visit = [ 0 for _ in range(N) ]
dist = [ 0 for _ in range(N) ]
cnt = 0

for _ in range(M):
    A, B = map(int, input().split())
    navi[A-1].append(B-1)
    
def bfs(start):
    global cnt
    
    deq = deque([start])
    visit[start] = 1
    
    while deq:
        v = deq.popleft()

        for i in navi[v]:
            if visit[i] == 0 :
                visit[i] = 1
                dist[i] = dist[v]+1
                deq.append(i)

bfs(X-1)
if K not in dist:
    print(-1)
else:
    # 오름차순대로 출력
    for i in range(N):
        if dist[i] == K:
            print(i+1)







