import sys
input = sys.stdin.readline
INF = 20000000

N = int(input())
M = int(input())

navi = [[ INF for _ in range(N) ] for _ in range(N)]
for _ in range(N):
    navi[_][_] = 0


for _ in range(M):
    i, j, weight = map(int, input().split())
    if navi[i-1][j-1] > weight:
        navi[i-1][j-1] = weight

for k in range(N):
    for i in range(N):
        for j in range(N):
            
            if navi[i][j] > navi[i][k] + navi[k][j]:
                navi[i][j] = navi[i][k] + navi[k][j]


for i in range(N):
    for j in range(N):
        if navi[i][j] == INF:
            navi[i][j]=0
        print(navi[i][j],end=' ')
    print()
    

