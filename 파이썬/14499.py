import sys
input = sys.stdin.readline


N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moveArr = list(map(int, input().split()))

dice = dict()
dice["BOTTOM"], dice["WEST"], dice["EAST"] = 0,0,0
dice["TOP"], dice["NORTH"], dice["SOUTH"] = 0,0,0

def moveDice(dir):
    if dir==1: # EAST
        dice["WEST"], dice["BOTTOM"], dice["EAST"], dice["TOP"] = dice["BOTTOM"], dice["EAST"], dice["TOP"], dice["WEST"]
    elif dir==2: # WEST
        dice["EAST"], dice["BOTTOM"], dice["WEST"], dice["TOP"] = dice["BOTTOM"], dice["WEST"], dice["TOP"], dice["EAST"]
    elif dir==3: # NORTH
        dice["SOUTH"], dice["BOTTOM"], dice["NORTH"], dice["TOP"] = dice["BOTTOM"], dice["NORTH"], dice["TOP"], dice["SOUTH"]
    elif dir==4: # WEST
        dice["NORTH"], dice["BOTTOM"], dice["SOUTH"], dice["TOP"] = dice["BOTTOM"], dice["SOUTH"], dice["TOP"], dice["NORTH"]

MOVE = [(0,1),(0,-1),(-1,0),(1,0)]

for dir in moveArr:
    nextX, nextY = x+MOVE[dir-1][0], y+MOVE[dir-1][1]
    if 0 <= nextX < N and 0 <= nextY < M:
        moveDice(dir)
        x,y = nextX, nextY

        if board[x][y]==0:
            board[x][y] = dice["BOTTOM"]
        else:
            dice["BOTTOM"] = board[x][y]
            board[x][y] = 0
        print(dice["TOP"])
