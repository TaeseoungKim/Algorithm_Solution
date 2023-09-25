import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
OPS = [list(map(int, input().split())) for _ in range(K)]
print(OPS)

for op in OPS:
    r, c, S = op
    
    #  (r-s, c-s)
     
    #   (r+s, c+s
    for s in range(1,S+1):
        for i in range(-s, s+1):
            board[r+i][c+i+1] = board[r+i][c+i]
            
            
            board[r+i][c+i] = board[r+i+1][c+i] = 
            
        
        
        #아래로 
        board[i][]
        
    break
