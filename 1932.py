import sys
input = sys.stdin.readline

N = int(input())
map_list = [ 0 for _ in range(N) ]

# 2차원 리스트에 입력 값을 모두 담는다
for _ in range(N):
    map_list[_] = list(map(int, input().split()))



if N==1:
    print(map_list[0][0])
else:
    for i in range(1,N):
        for j in range(i+1):
            #젤 왼쪽 값과 젤 오른쪽 값은 고려해야 할 값이 하나이다.
            if j == 0:
                map_list[i][j] += map_list[i-1][j]
            elif j == i:
                map_list[i][j] += map_list[i-1][j-1]
            #고려해야 할 값이 두 값이므로 둘 중 큰 값을 선택하여 갱신
            else:
                map_list[i][j] += max(map_list[i-1][j-1],map_list[i-1][j])
    print(max(map_list[N-1]))