import sys
input = sys.stdin.readline
N = int(input())
board = []

#상하좌우
move = [(-1,0),(1,0),(0,-1),(0,1)]
Teacher = []
result = False

for _ in range(N):
    board.append(list(input().split()))
print(board)

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            Teacher.append((i,j))

def compare(i,j):
    if board[i][j] == 'S':
        return -1
    elif board[i][j] == 'X':
        return 0
    elif board[i][j] == 'T' or board[i][j] == 'O': #확인필요
        return 1
    

#선생님의 상하좌우에 학생이 있는지 확인(걸린학생 있을 시 False리턴)
def check(i,j):
    #상하좌우
    for dy,dx in move:
        y=dy+i
        x=dx+j
        while 0<=y<N and 0<=x<N:
            if compare(y,x) == -1:
                return False
            elif compare(y,x) == 0:
                y += i
                x += j 
                continue
            else:
                break

    #걸린 학생없을 시 True리턴
    return True

def dfs(cnt):
    global result
    if cnt > 3:
        return
    if cnt == 3:
        for i,j in Teacher:
            if check(i,j):
                result = True
                return
            
    for i in range(N):
        for j in range(N):
            if board[i][j]=='X':
                board[i][j]='O'
                dfs(cnt+1)
                if result:
                    return
                board[i][j]='X'
                
        
        
dfs(0)
if result:
    print("YES")
else:
    print("NO")

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            