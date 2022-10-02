import sys
from collections import deque
input = sys.stdin.readline
MAX = 10**5

n, k = map(int, input().split())
visit = [0]*(MAX+1)

#시간을 구해야하는 문제는 방문한 시간을 남기면 된다.
def bfs():
    global n,k
    deq = deque()
    deq.append(n)

    while deq:
        pv = deq.popleft()
        if pv == k:
            print(visit[k])
            return
        for tmp in (pv+1,pv-1,pv*2):
            if not (0<= tmp <= MAX) :
                continue
            elif visit[tmp]==0:
                deq.append(tmp)
                visit[tmp]=visit[pv]+1

bfs()

