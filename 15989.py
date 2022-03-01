from collections import deque
t = int(input())
def dfs(v):
    #(1의 개수, 2의 개수, 3의 개수)
    visited[(v,0,0)]=1
    deq = deque()
    deq.append((v,0,0))
    cnt=0
    while deq:
        v1, v2, v3 = deq.pop()
        cnt+=1
        for next_v1, next_v2, next_v3 in [(v1-2,v2+1,v3),(v1-3,v2,v3+1)]:
            if 0<=next_v1 and 0<=next_v2 and 0<=next_v3 and (next_v1,next_v2,next_v3) not in visited.keys():
                visited[(next_v1,next_v2,next_v3)]=1
                deq.append((next_v1,next_v2,next_v3))
    return cnt

for _ in range(t):
    v = int(input())
    visited = dict()
    print(dfs(v))