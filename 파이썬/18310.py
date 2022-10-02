import sys
input = sys.stdin.readline
def func():
    N = int(input())
    house = sorted(list(map(int, input().split())))
    #최소값의 인덱스와 최소값을 minVal변수에 저장
    minVal = [-1,1e9]
    
    for i in range(N):
        dist_sum=0
        for j in range(N):
            dist_sum+=abs(house[j]-house[i])
            if minVal[1] > dist_sum:
                minVal[0] = i
                minVal[1] = dist_sum
    print(house(minVal[0]))
    
