# 자물쇠 영역의 합이 n*n이라면 정답.
# 한 구역이라도 2이상이면 돌기가 겹치는 것 이므로 건너뛴다.
def sum_check(key_board,board,n,m):
    sum = 0
    for i in range(0,n):
        for d in range(0,n):
            if board[i+m-1][d+m-1] + key_board[i+m-1][d+m-1] >= 2:
                return False
            else:
                sum += board[i+m-1][d+m-1] + key_board[i+m-1][d+m-1]
    if sum == n*n:
        return True
    else:
        return False
    
#0, 90, 180, 270도 바꿔가며 sum_check함수를 호출한다
def check(key_board,board,n,m):
    if sum_check(key_board,board,n,m)==True:
        return True
    for _ in range(3):
        tmp_keyboard = list([0]*(n+2*m-2) for _ in range(n+2*m-2))
        #90도 회전
        for i in range(n+2*m-2):
            for d in range(n+2*m-2):
                tmp_keyboard[d][n+2*m-3-i] = key_board[i][d]
        if sum_check(tmp_keyboard,board,n,m)==True:
            return True
        else: key_board=list(tmp_keyboard)
    return False

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # n+2*m-2크기의 board를 생성한다
    board = list([0]*(n+2*m-2) for _ in range(n+2*m-2))

    # 자물쇠를 보드의 가운데에 위치시킨다
    for i in range(0,n):
        for d in range(0,n):
            board[i+m-1][d+m-1]=lock[i][d]

    # 열쇠를 맨위왼쪽부터 이동시켜가며 체크한다
    for i in range(n+m-1):
        for d in range(n+m-1):
            key_board = list([0]*(n+2*m-2) for _ in range(n+2*m-2))
            for x in range(m):
                for y in range(m):
                    key_board[i+x][d+y] = key[x][y]
            
            if check(key_board,board,n,m) == True:
                return True
            else: 
                continue
    return False
                    
