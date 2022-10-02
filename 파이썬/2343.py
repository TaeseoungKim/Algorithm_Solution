import sys
input = sys.stdin.readline

N,M = map(int,input().split())
list = list(map(int , input().split()))

start,end = 1, sum(list)
answer = 0

def Search():
    global start,end,answer
    mid = (start+end)//2
    totalLength = mid
    cnt = 1 #블루레이의 수

    for length in(list):
        if length > mid :
            start = mid+1
            return
        elif totalLength-length < 0: 
            totalLength = mid 
            cnt += 1 
        totalLength -= length 
    
    if cnt > M :
        start = mid+1
    elif cnt <= M:
        end = mid-1
        answer = mid



while start <= end:
    Search()

print(answer)