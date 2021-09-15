import sys 
input = sys.stdin.readline

N, M = map(int,input().split())
list = list( int(input()) for _ in range(N) )
start, end = max(list) , sum(list)
answer = end

def Search():
    global start,end,answer
    mid = (start+end)//2
    myMoney = mid
    cnt = 1

    for value in(list):
        if myMoney - value < 0:
           cnt += 1
           myMoney = mid #인출

           if cnt > M:
            break
        
        myMoney -= value

    if cnt > M: # 오른쪽으로
        start = mid + 1
    elif cnt <= M: # 왼쪽으로
        answer = mid
        end = mid - 1

while start<=end :
    Search()
print(answer)








