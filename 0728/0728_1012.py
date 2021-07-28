# 제출시에 재귀에러가 나는데 왜 그런지 모르겟다..

T = int(input())

for idx_T in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    # 상하좌우
    d_row = [1, -1, 0, 0]
    d_column = [0, 0, -1, 1]
    earthworm_cnt = 0

    def dfs(row, column):
        board[row][column] = 0  # 방문처리

        for _ in range(4):
            tmp_row = d_row[_] + row
            tmp_column = d_column[_] + column

            if not(0 <= tmp_row < N and 0 <= tmp_column < M) :
                continue
            elif board[tmp_row][tmp_column] == 1:
                dfs(tmp_row,tmp_column)

    for i_k in range(K):
        column, row = map(int, input().split())
        board[row][column] = 1

    for i_row in range(N):
        for i_column in range(M):
            if board[i_row][i_column] == 1:
                earthworm_cnt += 1
                dfs(i_row, i_column)
            else:
                continue

    print(earthworm_cnt)