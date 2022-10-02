# 알고리즘은 해결했지만 제출시에 value 오류가 난다.
# 흠.. 리팩토링 필요
# 다른 로직이 있는가?

import sys
sys.setrecursionlimit(1000000)

length = int(input())

# 이런식으로 2차원을 입력받는다.
# 공백이 없는 입력을 받을 때는 => input().strip() 
board = [list(map(int, input().split())) for _ in range(length)] 


# board = [
# [6, 8, 2, 6, 2],
# [3, 2, 3, 4, 6],
# [6, 7, 3, 3, 2],
# [7, 2, 5, 3, 6],
# [8, 9, 5, 2, 7]
# ]

# 높이는 1 이상이다. 그러므로 방문한 인덱스는 0을 입력하여 방문 처리를 해준다.
# => 이러면 안된다. 높이에 따라 다시 사용해야 하기 때문

d_row = [1, -1, 0, 0]
d_col = [0, 0, -1, 1]

# 최대 높이 구하기
t_max = []
for _ in range(length):
    t_max.append(max(board[_]))
max_height = max(t_max)


def dfs(p_row, p_col, i_height):
    visit[p_row][p_col] = 1

    for i in range(4):
        tmp_row = d_row[i] + p_row
        tmp_col = d_col[i] + p_col

        if not(0 <= tmp_row < length and 0 <= tmp_col < length):
            continue
        elif board[tmp_row][tmp_col] > i_height and visit[tmp_row][tmp_col] == 0:
            dfs(tmp_row, tmp_col, i_height)


safe_area = []
for i_height in range(1, max_height, 1):
    visit = [[0] * length for _ in range(length)]
    area_cnt = 0
    for i_row in range(length):
        for i_col in range(length):
            if visit[i_row][i_col] == 1 or board[i_row][i_col] <= i_height :
                continue
            else:
                dfs(i_row, i_col, i_height)
                area_cnt += 1

    safe_area.append(area_cnt)

print(max(safe_area))
