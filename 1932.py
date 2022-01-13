import sys
input = sys.stdin.readline

N = int(input())
map_list = [ 0 for _ in range(N) ]

for _ in range(N):
    map_list[_] = list(map(int, input().split()))

if N==1:
    print(map_list[0][0])
else:
    for i in range(1,N):
        for j in range(i+1):
            if j == 0:
                map_list[i][j] += map_list[i-1][j]
            elif j == i:
                map_list[i][j] += map_list[i-1][j-1]
            else:
                map_list[i][j] += max(map_list[i-1][j-1],map_list[i-1][j])
    print(max(map_list[N-1]))