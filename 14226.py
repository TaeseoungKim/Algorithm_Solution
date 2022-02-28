#bfs를 사용할 때, 특징점(ex, 방법의 수, 경로의 수)도 같이 저장할 때는 visit의 원소를 2개 사용한다. (ex, [-1,0])
#bfs에서 최단시간을 구할 때, popleft를 쓰므로, 처음 pop된 시간이 최단시간이다.
#deque에 튜플을 넣을 때는, append를 해준다.
from collections import deque
def bfs():
    visit = dict()
    visit[(1,0)]=0 # (화면 이모티콘 수, 클립보드 이모티콘 수)
    deq = deque()
    deq.append((1,0))
    while deq:
        m, c = deq.popleft()
        if m==k: return visit[(m,c)]
        if (m-1,c) not in visit.keys():
            visit[(m-1,c)]=visit[(m,c)]+1
            deq.append((m-1,c))
        if (m,m) not in visit.keys():
            visit[(m,m)]=visit[(m,c)]+1
            deq.append((m,m))
        if (m+c,c) not in visit.keys():
            visit[(m+c,c)]=visit[(m,c)]+1
            deq.append((m+c,c))
k = int(input())
print(bfs())