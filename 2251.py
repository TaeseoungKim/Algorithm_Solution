
from collections import deque
import sys
input = sys.stdin.readline
#c의 물의 양은 a,b의 상태에 따라 결정된다
#전체-(a+b)=c
a,b,c = map(int, input().split())
total = a+b+c
visit = [[0]*(c+1) for _ in range(c+1)]
result = [0]*(c+1)
def bfs():
    deq = deque()
    deq.append((0,0))
    
    while deq:
        pa,pb = deq.popleft()
        if pa==0: result[c-pb]=1

        if visit[pa][pb]==1:
            continue
        else:
            visit[pa][pb]=1

        #a->b
        if pa-(b-pb)<=0:#a를 모두 비움
           deq.append((0,pa+pb))
        else: #b가 꽉참
            deq.append((pa-(b-pb),b))

        #b->a
        if pb-(a-pa)<=0:#b를 모두 비움
           deq.append((pa+pb,0))
        else:#a가 꽉참
            deq.append((a,pb-(a-pa)))
        
        
        #c->a
        if c-a-pb<=0:#c를 모두 비움
           deq.append((c-pb,pb))
        else:#a가 꽉참
            deq.append((a,pb))

        #c->b
        if c-b-pa<=0:#c를 모두 비움
           deq.append((pa,c-pa))
        else:#b가 꽉참
            deq.append((pa,b))

        deq.append((pa,0)) #b->c
        deq.append((0,pb)) #a->c

bfs()
for i in range(1,c+1):
    if result[i]==1:
        print(i,end=" ")