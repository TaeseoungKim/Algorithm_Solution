from collections import deque
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
visit = [[0]*(b+1) for i in range(a+1)]

def pour(ta,tb,deq):
    if visit[ta][tb]==1:
        return False
    else: 
        visit[ta][tb]=1
        deq.append((ta,tb))
        return True
result = [0]*(c+1)

def bfs(water):
    deq = deque()
    deq.append(water)
    while deq:
        pa,pb = deq.pop()
        if pa==0:
            result[c-pa-pb]=1
            
        #빠지고 들어오는 양은 동일하므로 water변수에 담는다
        #a->b
        water = min(pa,b-pb)
        pour(pa-water,pb+water,deq)
        
        #a->c
        water = pa
        pour(0,pb,deq)
        
        #b->a
        water = min(a-pa,pb)
        pour(pa+water,pb-water,deq)

        #b->c
        water = pb
        pour(pa,0,deq)
        
        #c->a
        water = min(a-pa,c-(pa+pb))
        pour(pa+water,pb,deq)

        #c->b
        water = min(b-pb,c-(pa+pb))
        pour(pa,pb+water,deq)

bfs((0,0))
for i in range(0,c+1):
    if result[i]==1:
        print(i,end=" ")