from collections import deque

def solution(costs, xcost, ycost):
    costX = ycost
    costY = xcost

    n = len(costs)
    m = len(costs[0])

    board = [[0 for d in range(m)] for i in range(n)]
    visited = [[False for d in range(m)] for i in range(n)]
    board[0][0] = costs[0][0]

    def bfs(pos):
        queue = deque()
        queue.append(pos)
        visited[0][0] = True

        while queue:
            px,py = queue.popleft()
            for tx,ty,XY in [(px+1,py,1),(px,py+1,2)]:
                if 0<=tx<n and 0<=ty<m:

                    if XY==1 :
                        if visited[tx][ty]==False:
                            visited[tx][ty]=True
                            board[tx][ty] = board[px][py]+costs[tx][ty]-costX
                            queue.append((tx,ty))   

                        elif (board[px][py]+costs[tx][ty]-costX)>board[tx][ty]:
                            board[tx][ty]= board[px][py]+costs[tx][ty]-costX
                            queue.append((tx,ty))

                    if XY==2:
                        if visited[tx][ty]==False:
                            visited[tx][ty]=True
                            board[tx][ty] = (board[px][py]+costs[tx][ty]-costY)
                            queue.append((tx,ty))

                        elif (board[px][py]+costs[tx][ty]-costY)>board[tx][ty]:
                            board[tx][ty] = (board[px][py]+costs[tx][ty]-costY)
                            queue.append((tx,ty))


    bfs((0,0))

    maxV = max(board[n-1])
    if maxV<=0:
        return 0
    else:
        return maxV 