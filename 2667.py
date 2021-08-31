from collections import deque

def bfs(x,y):

    if board[y][x] == 0 :
        return

    board[y][x] = 0
    deq = deque()
    deq.append( (x,y) )    
    count = 1

    while deq.__len__() != 0 :
        pop_x , pop_y = deq.popleft()

        for i in range(4):
            tmp_x = pop_x + dx[i]
            tmp_y = pop_y + dy[i]

            if ( 0 <= tmp_x < n and 0 <= tmp_y < n ) != True:
                continue
            elif board[tmp_y][tmp_x] == 1 :
                board[tmp_y][tmp_x] = 0
                deq.append( (tmp_x,tmp_y) )
                count += 1

    house_list.append(count)

n = int(input())

board = [ list(map(int, input())) for _ in range(n) ]  #체크
#board = [ [0,1,1,0,1,0,0] , [1,1,1,0,1,0,0] ,[0,1,1,0,1,0,0] , [0,1,1,0,1,0,0], [0,1,1,0,1,0,0], [0,1,1,0,1,0,1], [0,1,1,0,1,0,0] ]
house_list = []

dy = [ 1 , -1 , 0 , 0 ]
dx = [ 0 , 0 , -1 , 1 ]

for x in range(n):
    for y in range(n):
        bfs(x,y)

house_list.sort()

print(house_list.__len__())
for _ in range(house_list.__len__()):
    print( house_list[_] )
                
                

