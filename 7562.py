from collections import deque

testCase = int(input())

for _ in range(testCase):
        
    length = int(input())
    start_x, start_y = map(int , input().split())
    end_x, end_y = map(int , input().split())

    dx = [ -2, -1, 1, 2, -2, -1, 1, 2 ]
    dy = [ 1, 2, 2, 1, -1, -2, -2, -1]

    board = [ [0] * length for _ in range(length) ]
    visit = [ [0] * length for _ in range(length) ]
    is_found = 0

    deq = deque()
    deq.append( (start_x,start_y) )

    if start_x == end_x and start_y == end_y :
        print(0)
        continue

    while deq.__len__() != 0 :
        pop_x , pop_y = deq.popleft()

        for _ in range(8):
            tmp_x = pop_x + dx[_]
            tmp_y = pop_y + dy[_]

            if (0 <= tmp_x < length and 0 <= tmp_y < length) != True :
                continue            
            elif visit[tmp_x][tmp_y] == 0 and board[tmp_x][tmp_y] == 0:
                deq.append( (tmp_x,tmp_y) )
                visit[tmp_x][tmp_y] = visit[pop_x][pop_y] + 1

            if tmp_x == end_x and tmp_y == end_y:
                is_found = 1
                break
        
        if is_found == 1:
            print(visit[end_x][end_y])
            break

        





