import sys
input = sys.stdin.readline

N = int(input())
list = list( map(int, input().split()) )
M = int(input())
answer = 0

start , end = 0 , max(list)

def Search():
    global start,end,answer
    mid = (start+end)//2
    budget = M

    for value in(list):
   
        
        if mid < value:
            budget -= mid    
        elif mid >= value:
            budget -= value

    if budget >= 0 :
        start = mid + 1
        answer = mid
    elif budget < 0 :
        end = mid - 1

if M >= sum(list):
    print(max(list))
else:
    while start <= end:
        Search()
    print(answer)