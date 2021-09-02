import sys

_ , C = map(int,input().split())
N = sorted(list( int(sys.stdin.readline()) for _ in range(_)))

# 가장 인접한 두 공유기 사이의 '거리'를 구하는 것이기 때문에 
# 최소값과  최대값을 각각 1,  N[-1] - N[0]로 지정
start = 1
end = N[-1] - N[0]
result = 0

while start <= end :
    # 1부터 설치
    mid = (start+end) // 2
    current = N[0]
    cnt = 1
    
    #모든 좌표에 대하여 검사
    for i in range(len(N)):
        if N[i] >= current + mid:
            cnt += 1
            current = N[i]
    
    if cnt >= C:
        result = mid
        start = mid + 1

    else:
        end = mid - 1
    
print(result)






