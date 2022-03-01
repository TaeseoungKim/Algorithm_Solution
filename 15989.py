from collections import deque
import sys
sys.setrecursionlimit(10**5)
t = int(input())
def dfs(v1,v2,v3):
    #(1의 개수, 2의 개수, 3의 개수)
    global cnt
    cnt+=1
    visited[(v1,v2,v3)]=1
    for next_v1, next_v2, next_v3 in [(v1-2,v2+1,v3),(v1-3,v2,v3+1)]:
        if 0<=next_v1 and 0<=next_v2 and 0<=next_v3 and (next_v1,next_v2,next_v3) not in visited.keys():
            visited[(next_v1,next_v2,next_v3)]=1
            dfs(next_v1, next_v2, next_v3)

for _ in range(t):
    v = int(input())
    visited = dict()
    cnt=0
    dfs(v,0,0)
    print(cnt)