import sys
input = sys.stdin.readline

board = list(list(map(int, input().strip())) for _ in range(9))
for _ in range(9):
    print(board[_])
    
def dfs(x,y):
    return


# 열체크
# 행체크
# 3x3체크 나머지,,,