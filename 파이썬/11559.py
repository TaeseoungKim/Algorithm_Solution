from collections import deque
import sys
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]

def gravity():
    for y in range(6):
        blank = deque()
        for x in range(11,-1,-1):
            if board[x][y]==".":
                blank.append(x)
            if blank and board[x][y] in ["R","Y","G","B","P"]:
                pb = blank.popleft()
                board[pb][y],board[x][y] = board[x][y],board[pb][y]
                blank.append(x)

def bfs(x_,y_,color):
    visited[x_][y_]=1
    deq=deque()
    deq.append((x_,y_))
    boom = deque()
    cnt=0
    while deq:
        x,y = deq.popleft()
        boom.append((x,y))
        cnt+=1
        for next_x, next_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=next_x<12 and 0<=next_y<6:
                if visited[next_x][next_y]==0 and board[next_x][next_y]==color:
                    deq.append((next_x,next_y))
                    visited[next_x][next_y]=1
    if cnt>=4:
        for x,y in boom:
            board[x][y]='.'
        return True
result = 0
while True:
    visited = [[0]*6 for _ in range(12)]
    tmp=0
    for i in range(12):
        for d in range(6):
            if visited[i][d]==1:
                continue
            if board[i][d]=='R' and bfs(i,d,'R'):
                tmp+=1
            elif board[i][d]=='Y' and bfs(i,d,'Y'):
                tmp+=1
            elif board[i][d]=='G' and bfs(i,d,'G'):
                tmp+=1
            elif board[i][d]=='B' and bfs(i,d,'B'):
                tmp+=1
            elif board[i][d]=='P' and bfs(i,d,'P'):
                tmp+=1
    if tmp==0:
        break
    else: result+=1
    gravity()

print(result)