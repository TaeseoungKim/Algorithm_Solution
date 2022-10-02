import sys
sys.setrecursionlimit(1000000)

def dfs(i_row,i_col,board,max_row,max_col):
    board[i_row][i_col] = 0
    
    for i in range(8):
        tmp_row = d_row[i] + i_row
        tmp_col = d_col[i] + i_col
    
        if not(0 <= tmp_row < max_row and 0 <= tmp_col < max_col) :
            continue
        elif board[tmp_row][tmp_col] == 1:
            dfs(tmp_row,tmp_col,board,max_row,max_col)

# 상 하 좌 우 왼대 오대
d_row = [ 1 , -1 , 0 , 0 , 1 , 1 , -1 , -1]
d_col = [ 0 , 0 , -1 , 1 , -1 , 1 , -1 , 1 ]


while True:
    max_col , max_row = map(int , input().split())

    if max_col == 0 and max_row == 0:
        break

    board = [ list(map(int, input().split())) for _ in range(max_row) ]
    island_cnt = 0


    for i_row in range(max_row):
        for i_col in range(max_col):
            if board[i_row][i_col] == 0:
                continue
            else:
                dfs(i_row,i_col,board,max_row,max_col)
                island_cnt += 1
    
    print(island_cnt)