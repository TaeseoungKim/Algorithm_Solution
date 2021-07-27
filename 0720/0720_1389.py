from collections import deque


def bfs(v):
    visit = [ 0 for _ in range(n) ] 
    visit[v] = 1 
    deq = deque() 
    deq.append(v) 

    while deq.__len__() != 0 :
        pop_x = deq.popleft()
        
        for i in range(n):
            if visit[i] == 0 and list[pop_x][i] == 1 :
                deq.append(i)
                visit[i] = 1
                path_length[v][i] = path_length[v][pop_x] + 1 

    for i in range(n):
        sumOf_path[v] = sumOf_path[v] + path_length[v][i]

    
n , m = map(int , input().split() )
list = [ [0] * n for _ in range(n) ]
path_length = [ [0] * n for _ in range(n) ]
sumOf_path = [ 0 for _ in range(n) ]

for _ in range(m):
   node_1 , node_2 = map( int , input().split() )
   list[node_1-1][node_2-1] = list[node_2-1][node_1-1] = 1

for _ in range(n):
    bfs(_)


print( sumOf_path.index( min(sumOf_path) ) + 1 )


