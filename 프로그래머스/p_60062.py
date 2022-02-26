

from collections import deque


# n=12
# weak=[1, 5, 6, 10]	
# dist=[1, 2, 3, 4]

def dfs(n,i,d,visit,dist,dist_visited):
    visit[i:dist[d]] = 1
    dist_visited[d] = 1

    for x in range(n):
        if visit[x]==0:
            dfs(n,i,d,visit,dist,dist_visited)
            dist_visited

    deq=deque()
    deq.append((i,d))
    while deq:
        x,y = deq.pop()


    return

def solution(n, weak, dist):
    n=12
    weak=[1, 5, 6, 10]	
    dist=[1, 2, 3, 4]

    distlen = len(dist)

    
    for i in range(n):
        for d in range(distlen):
            visit = [0]*n
            dist_visited = [0]*len(dist)
            dfs(i,d,visit,dist,dist_visited)

    answer = 0
    return answer

# solution(n,weak,dist)









