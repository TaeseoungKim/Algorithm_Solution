n=int(input())
board = [0]*1001
board[1]=1
board[2]=2
for i in range(3,n+1):
    board[i]=board[i-1]+board[i-2]
print(board[n]%10007)
