import sys
input = sys.stdin.readline

quack = input().strip()
board = [0]*5
isWrong=False
answ=0

for c in quack:
    if c=='q':
        board[0]+=1
        if board[0]>answ:
            answ+=1
    elif c=='u':
        if board[1]>=board[0]:
            isWrong=True
        else: board[1]+=1
    elif c=='a':
        if board[2]>=board[1]:
            isWrong=True
        else: board[2]+=1
    elif c=='c':
        if board[3]>=board[2]:
            isWrong=True
        else: board[3]+=1
    elif c=='k':
        if board[4]>=board[3]:
            isWrong=True
        else: 
            board[4]+=1
            for i in range(5):
                board[i]-=1

for i in range(5):
    if board[i]!=0:
        isWrong=True
        break
if isWrong: print(-1)
else: print(answ)