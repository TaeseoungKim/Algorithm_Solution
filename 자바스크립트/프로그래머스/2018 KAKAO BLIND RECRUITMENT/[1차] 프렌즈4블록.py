def calGrade(i, d, board, m, n, visited):
    char = board[i][d]
    grade = 0
    if i == m-1 or d == n-1:
        return grade
    if board[i+1][d+1] == char and board[i+1][d] == char and board[i][d+1] == char:
        if visited[i][d] == False:
            grade += 1
            visited[i][d] = 1

        if visited[i+1][d] == False:
            grade += 1
            visited[i+1][d] = 1

        if visited[i][d+1] == False:
            grade += 1
            visited[i][d+1] = 1

        if visited[i+1][d+1] == False:
            grade += 1
            visited[i+1][d+1] = 1
    return grade


def solution(m, n, board):
    grade = 0
    cnt = 0

    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]
        tempGrade = 0

        cnt += 1
        if cnt == 4:
            break

        for i in range(m):
            for d in range(n):
                if board[i][d] == 0:
                    continue
                tempGrade += calGrade(i, d, board, m, n, visited)

        grade += tempGrade
        if tempGrade == 0:
            break

        board = downBlocks(board, m, n, visited)
    return grade


def downBlocks(board, m, n, visited):
    tempBoard = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        tempIdx = m-1
        for d in range(m-1, -1, -1):
            if visited[d][i] == 1:
                continue
            else:
                tempBoard[tempIdx][i] = board[d][i]
                tempIdx -= 1
    return tempBoard
