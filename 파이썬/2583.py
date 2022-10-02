from collections import deque

dy = [ -1 , 1 , 0 , 0]
dx = [ 0, 0, -1, 1 ]

def bfs(y,x):
    
    if visit[y][x] == 1 or Nemo[y][x] == 1:
        return

    else :
        area = 1 # 빈 공간
        visit[y][x] = 1
        deq = deque()
        deq.append( (y,x) )

        while deq.__len__() != 0 :
            
            pop_y, pop_x = deq.popleft()
            for _ in range(4) :
                tmp_y = pop_y + dy[_]
                tmp_x = pop_x + dx[_]
                if 0 <= tmp_y < m and 0 <= tmp_x < n:
                    if visit[tmp_y][tmp_x] == 0 and Nemo[tmp_y][tmp_x] == 0:
                        deq.append( (tmp_y,tmp_x) )
                        visit[tmp_y][tmp_x] = 1
                        area += 1

        area_list.append(area)


m , n , k = map(int, input().split())

# 네모 ㅋㅋ
Nemo = [[0] * (n) for _ in range(m)]
visit = [[0] * (n) for _ in range(m)]
area_list = []

for _ in range(k):
    dx_1, dy_1, dx_2, dy_2 = map(int, input().split())
    for from_dx in range(dx_1,dx_2,1):
        for from_dy in range(dy_1,dy_2,1):
            Nemo[from_dy][from_dx] = 1



for y in range(m):
    for x in range(n):
        bfs(y,x)

area_list.sort()
print(area_list.__len__())

for _ in range(area_list.__len__()):
    print(area_list[_],end=" ")
