import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
for i in range(N):
    board[i] -= 1

lastIndex = -1
answer = 0

def backTracking(curIdx, maxNum, count):
    global answer, lastIndex
    if answer < count: 
        lastIndex = curIdx
        answer =  count
    elif lastIndex <= curIdx and count < answer:
         return

    for i in range(curIdx+1,N):
            if maxNum < board[i]:
                backTracking(i,board[i],count+1)

for i in range(N):
    backTracking(i,board[i],1)
print(answer)