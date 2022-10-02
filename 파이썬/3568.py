import sys
input = sys.stdin.readline
board = input().split()
board_len = list(map(len, board))
result = [str(board[0]) for _ in range(1,len(board))]

for i in range(1,len(board)):
    type = 0    
    for d in range(board_len[i]-1,-1,-1):
        if board[i][d]==',' or board[i][d]==';':continue
        elif board[i][d] == '&' or board[i][d] == '*' :
            result[i-1]+=str(board[i][d])
        elif  board[i][d] == ']':
            result[i-1]+=str("[]")
            d+=1
        elif not(board[i][d] == '&' or board[i][d] == '*' or board[i][d] == '[' or board[i][d] == ']'):
            type=d
            break
    result[i-1]+=' '
    for d in range(0,d+1):
        result[i-1]+=str(board[i][d])
    result[i-1]+=';'
for i in range(len(board)-1):
    print(result[i])