# 모든 경로를 연결해야 한다...
# 크루스칼 해도 괜찮을 것 같은데

INF = 2e9


def solution(V, road, branch):

    board = [[INF for _ in range(V+1)] for _ in range(V+1)]
    for v in road:
        x, y, wei = v
        board[x][y] = wei
        board[y][x] = wei

    for i in range(1, V+1):
        board[i][i] = 0

    for i in range(1, V+1):
        for d in range(1, V+1):
            for k in range(1, V+1):
                board[i][d] = min(board[i][d], board[i][k]+board[k][d])
                board[d][i] = min(board[d][i], board[d][k]+board[k][i])
    answ = []
    for i in range(1, V+1):
        minV, minBranch = INF, -1
        for idx, val in enumerate(branch):
            if minV > board[i][val]:
                minV = board[i][val]
                minBranch = val
        answ.append(minBranch)

    return answ
