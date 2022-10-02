n=int(input())
board = [0]*(n+1)
board[1]=1
if n==1:
    print(1)
else:
    board[2]=3
    if n==2:
        print(board[n])
    else:
        for i in range(3,n+1):
            board[i]=board[i-1]+board[i-2]*2
        print(board[n]%10007)
