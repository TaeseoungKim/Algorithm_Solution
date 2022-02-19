import sys
input = sys.stdin.readline
n, k = map(int, input().split())
board=[0,0]
for n in range(2,n+1):
    board.append(1)
cnt, answer= 0,0

for i in range(len(board)):
    if board[i]==1:
        for d in range(i,n+1,i):
            if board[d]!=0:
                cnt += 1
                board[d]=0

            if cnt==k:
                answer=d
                break
    if answer!=0:
        print(answer)
        break