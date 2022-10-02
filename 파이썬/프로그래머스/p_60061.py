
#설치 가능한지 검사 (d가 true면 삭제가능한지 검사)
def check(x,y,a,board,delete):
    if delete==True and board[x][y][a]==False:
        return True
    if a==0: #기둥
        #바닥면이거나, 기둥위에 있거나, 보의 끝 부분 위에 있을 경우 가능
        if y==0 or board[x][y-1][0] or (x!=0 and board[x-1][y][1]) or board[x][y][1]:
            return True
    elif a==1: #보
        #기둥위에 있거나, 보의 끝 부분 위에 있을 경우 가능
        if board[x][y-1][0] or board[x+1][y-1][0] or ((x!=0 and board[x-1][y][1]) and board[x+1][y][1]):
            return True
    return False

def solution(n, build_frame):
    # board[][]의 첫 원소는 기둥, 두번째 원소는 보를 의미
    board = list([list([False,False]) for _ in range(n+1)] for _ in range(n+1))
    
    for x,y,a,b in build_frame:
        if b==0: #삭제일 경우
            board[x][y][a] = False
            if a==0:
                if not(check(x,y+1,0,board,True) and check(x,y+1,1,board,True) and check(x-1,y+1,1,board,True)):
                    board[x][y][a] = True
                    continue
            elif a==1:
                if not(check(x,y,0,board,True) and check(x+1,y,0,board,True) and check(x-1,y,1,board,True) and check(x+1,y,1,board,True)):
                    board[x][y][a] = True
                    continue
        elif b==1: #설치일 경우
            if a==0: #기둥
                #바닥면이거나, 기둥위에 있거나, 보의 끝 부분 위에 있을 경우 가능
                if check(x,y,a,board,False):
                    board[x][y][0]=True
            elif a==1: #보
                #기둥위에 있거나, 보의 끝 부분 위에 있을 경우 가능
                if check(x,y,a,board,False):
                    board[x][y][1]=True       
    answer = []
    for i in range(n+1):
        for d in range(n+1):
            if board[i][d][0]==True:
                answer.append([i,d,0])
            if board[i][d][1]==True:
                answer.append([i,d,1])
    return answer