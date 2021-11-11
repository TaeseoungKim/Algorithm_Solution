import sys
input = sys.stdin.readline

X , Y = map(int,input().split())
winRate = int((Y / X) * 100)
answer = 0

start , end = 1 , X
# end를 X로 잡는것이 맞는지는 모르겟다.

def Search():
    global start,end,winRate,answer
    mid = (start+end) // 2
    
    predict_total = X + mid
    predict_win = Y + mid
    predict_winRate = int((predict_win/predict_total)*100)

    if predict_winRate > winRate:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

    
while start <= end:
    Search()    

if answer != 0:
    print(answer)
else:
    print(-1)
