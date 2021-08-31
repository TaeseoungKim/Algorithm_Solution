from collections import deque

def bfs():
    Added_tomato = [0, 0]  # 날이 지나가면서 추가로 익은 토마토의 개수를 저장한다.
    count = 0
    day = 0  # 진행되고 있는 날짜 계산
    zero_count = 0  # 익지 않은 토마토 계산

    # 함수가 실행되면 모든 익은 토마토들을 append해준다
    for x in range(m):
        for y in range(n):
            if tomato_box[y][x] == 1:
                deq.append((x, y))
                Added_tomato[0] += 1
            elif tomato_box[y][x] == 0:
                zero_count += 1

    while deq.__len__() != 0:
        pop_x, pop_y = deq.popleft()
        count += 1

        for i in range(4):
            tmp_x = pop_x + dx[i]
            tmp_y = pop_y + dy[i]

            if (0 <= tmp_x < m and 0 <= tmp_y < n) != True:
                continue
            elif tomato_box[tmp_y][tmp_x] == 0:
                zero_count -= 1
                Added_tomato[day+1] += 1
                deq.append((tmp_x, tmp_y))
                tomato_box[tmp_y][tmp_x] = 1

        if count == Added_tomato[day]:
            count = 0
            day += 1
            Added_tomato.append(0)

    if zero_count == 0:
        print(day-1)
    else:
        print(-1)


m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]  # 체크
deq = deque()


# 상하좌우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

bfs()
