from collections import deque

def bfs():
    deq = deque()
    deq.append((0, 0))  # (0,0) 부터 시작한다.
    visit[0][0] = 1

    is_end = 0

    while deq.__len__() != 0:
        row, column = deq.popleft()

        for _ in range(4):
            tmp_row = row + d_row[_]
            tmp_column = column + d_column[_]
            if (0 <= tmp_row < n and 0 <= tmp_column < m) != True:
                continue
            elif visit[tmp_row][tmp_column] == 0 and graph[tmp_row][tmp_column] == 1:
                deq.append((tmp_row, tmp_column))
                visit[tmp_row][tmp_column] =  visit[row][column] + 1 # 체크

            if tmp_row == n-1 and tmp_column == m-1:
                is_end = 1
                break

        if is_end == 1:
            break


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]  # 체크
visit = [[0] * m for _ in range(n)]

d_row = [-1, 1, 0, 0]  # 상하
d_column = [0, 0, -1, 1]  # 좌우

bfs()
print( visit[n-1][m-1] )
