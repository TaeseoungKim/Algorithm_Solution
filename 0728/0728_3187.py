import sys
sys.setrecursionlimit(1000000)

low, column = map(int, input().split())
board = [list(input().strip()) for _ in range(low)]
visit = [[0] * (column) for _ in range(low)]

# 상하좌우
d_low = [1, -1, 0, 0]
d_column = [0, 0, -1, 1]

# 더 보기 좋게, 깔끔하게 변수를 정리할 수 있는 방법이 있나?
wolf_cnt = 0
sheep_cnt = 0
wolf_survived = 0
sheep_survived = 0


def dfs(v_low, v_column):
    global wolf_cnt
    global sheep_cnt

    if visit[v_low][v_column] == 1 or board[v_low][v_column] == '#':
        return
    elif board[v_low][v_column] == 'v':
        wolf_cnt += 1
    elif board[v_low][v_column] == 'k':
        sheep_cnt += 1

    visit[v_low][v_column] = 1

    for i in range(4):
        tmp_low = d_low[i] + v_low
        tmp_column = d_column[i] + v_column

        if not(0 <= tmp_low < low and 0 <= tmp_column < column):
            continue
        elif visit[tmp_low][tmp_column] == 1:
            continue
        elif board[tmp_low][tmp_column] == '#':
            continue
        elif board[tmp_low][tmp_column] == '.' or board[tmp_low][tmp_column] == 'v' or board[tmp_low][tmp_column] == 'k':
            dfs(tmp_low, tmp_column)

    return


for i_low in range(low):
    for i_column in range(column):

        if board[i_low][i_column] == '#':
            continue
        elif visit[i_low][i_column] == 0:
            dfs(i_low, i_column)

        if sheep_cnt == 0 and wolf_cnt == 0:
            pass
        elif sheep_cnt > wolf_cnt:
            sheep_survived += sheep_cnt
        else:
            wolf_survived += wolf_cnt

        wolf_cnt = 0
        sheep_cnt = 0


print(sheep_survived, wolf_survived)
