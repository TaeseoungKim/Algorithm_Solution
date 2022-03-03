import sys
input = sys.stdin.readline

number0 = {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):0, (1,2):1, (2,0):1, (2,1):0, (2,2):1, (3,0):1, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number1 = {(0,0):1, (0,1):0, (1,0):1, (1,1):0, (2,0):1, (2,1):0, (3,0):1, (3,1):0, (4,0):1, (4,1):0}
number2 = {(0,0):1, (0,1):1, (0,2):1, (1,0):0, (1,1):0, (1,2):1, (2,0):1, (2,1):1, (2,2):1, (3,0):1, (3,1):0, (3,2):0, (4,0):1, (4,1):1, (4,2):1,}
number3 = {(0,0):1, (0,1):1, (0,2):1, (1,0):0, (1,1):0, (1,2):1, (2,0):1, (2,1):1, (2,2):1, (3,0):0, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number4 = {(0,0):1, (0,1):0, (0,2):1, (1,0):1, (1,1):0, (1,2):1, (2,0):1, (2,1):1, (2,2):1, (3,0):0, (3,1):0, (3,2):1, (4,0):0, (4,1):0, (4,2):1,}
number5 = {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):0, (1,2):0, (2,0):1, (2,1):1, (2,2):1, (3,0):0, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number6 = {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):0, (1,2):0, (2,0):1, (2,1):1, (2,2):1, (3,0):1, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number7 = {(0,0):1, (0,1):1, (0,2):1, (1,0):0, (1,1):0, (1,2):1, (2,0):0, (2,1):0, (2,2):1, (3,0):0, (3,1):0, (3,2):1, (4,0):0, (4,1):0, (4,2):1,}
number8 = {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):0, (1,2):1, (2,0):1, (2,1):1, (2,2):1, (3,0):1, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number9 = {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (1,1):0, (1,2):1, (2,0):1, (2,1):1, (2,2):1, (3,0):0, (3,1):0, (3,2):1, (4,0):1, (4,1):1, (4,2):1,}
number_dict = [number0,number1,number2,number3,number4,number5,number6,number7,number8,number9]
def isOne(d,number_board):
    for row in range(5):
        for column in range(2):
            if number1[(row,column)]!=number_board[row][d+column]:
                return False
    return True
    
def search(d,number_board):
    #1인지 먼저 검사
    if isOne(d,number_board):
        for i in range(d,d+2):
            visited[i]=1
        return str('1')
    #방문처리
    for i in range(d,d+3):
        visited[i]=1

    for n in range(0,10):
        if n==1: continue
        isnot = 0
        for row in range(5):
            for column in range(3):
                if number_dict[n][(row,column)]!=number_board[row][d+column]:
                    isnot=1
                    break
            if isnot==1:
                break
        if isnot==0:
            return str(n)
    return " "

n = int(input())
board = input()
row = n//5
number_board = [[0]*(row+1) for _ in range(5)]
visited = [0]*(row+1)
for i in range(5):
    for d in range(row):
        if board[i*row+d]=='#':
            number_board[i][d] = 1
result = ""
for d in range(row):
        if visited[d] == 0 and board[d]=='#':
            result += search(d,number_board)
print(result)