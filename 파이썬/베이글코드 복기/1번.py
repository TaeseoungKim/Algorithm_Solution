from collections import deque


def solution(width, height, diagonals):
    diaInfo = [[[False, False]
                for d in range(width+1)] for i in range(height+1)]
    visited = [[False for d in range(width+1)] for i in range(height+1)]
    answer = 0

    for y, x in diagonals:
        # 오른쪽으로 이어지는 대각선
        diaInfo[x][y-1][0] = True
        # 대각선으로 이어지는 대각선
        diaInfo[x-1][y][1] = True

    def bfs(pos, visited, used):
        nonlocal answer
        x, y = pos[0], pos[1]

        if x == height and y == width:
            answer += 1
            return

        if diaInfo[x][y][0] == False and diaInfo[x][y][1] == False:
            for tx, ty in [(x+1, y), (x, y+1)]:
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, used)
                    visited[tx][ty] = False

        elif diaInfo[x][y][0] == True and diaInfo[x][y][1] == True:
            for tx, ty in [(x+1, y), (x, y+1)]:
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, used)
                    visited[tx][ty] = False

            if used == False:
                for tx, ty in [(x-1, y+1), (x+1, y-1)]:
                    if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                        visited[tx][ty] = True
                        bfs((tx, ty), visited, True)
                        visited[tx][ty] = False

        elif diaInfo[x][y][0] == True and diaInfo[x][y][1] == False:
            for tx, ty in [(x+1, y), (x, y+1)]:
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, used)
                    visited[tx][ty] = False
            if used == False:
                tx, ty = x-1, y+1
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, True)
                    visited[tx][ty] = False

        elif diaInfo[x][y][1] == True and diaInfo[x][y][0] == False:

            for tx, ty in [(x+1, y), (x, y+1)]:
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, used)
                    visited[tx][ty] = False

            if used == False:
                tx, ty = (x+1, y-1)
                if 0 <= tx <= height and 0 <= ty <= width and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    bfs((tx, ty), visited, True)
                    visited[tx][ty] = False

    visited[0][0] = True
    bfs((0, 0), visited, False)
    visited[0][0] = False
    return answer % 10000019
