import sys
input = sys.stdin.readline
n,k = map(int, input().split())
bag = [ list(map(int, input().split())) for _ in range(n)]
visited = [0]*(n+1)
max_V = 0
def solution(idx,wei,v):
    global max_V
    if k<wei:
        max_V = max(max_V,v-bag[idx][1])
        return
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            solution(i,wei+bag[i][0],v+bag[i][1])
            visited[i]=0
tmp_w=0
tmp_v=0
for i in range(n):
    tmp_w+=bag[i][0]
    tmp_v+=bag[i][1]
if tmp_w<=k:
    print(tmp_v)
else:
    solution(0,0,0)
    print(max_V)