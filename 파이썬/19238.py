import sys
from collections import deque
input = sys.stdin.readline

N, M, curGas = map(int, input().split())
board = [list(map(int, input().split(" "))) for _ in range(N)] # 0은 빈칸, 1은 벽
taxi = tuple(map(int, input().split()))
taxi = (taxi[0]-1,taxi[1]-1)
client = dict()

for i in range(M):
    sx, sy, dx, dy = map(int, input().split(" "))
    client[(sx-1,sy-1)] = (dx-1,dy-1)
    board[sx-1][sy-1] = -1 # -1은 승객

def searchClient(pos):
    if pos in client:
        return [(pos[0],pos[1],0)]
    deq = deque()
    deq.append(pos)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[pos[0]][pos[1]] = 1
    minV = sys.maxsize
    nextClient = []
    
    while deq:
        px, py = deq.popleft()
        for nx, ny in [(px+1,py),(px,py+1),(px-1,py),(px,py-1)]:
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]==0 and board[nx][ny]!=1:
                visited[nx][ny] = visited[px][py] + 1
                deq.append((nx,ny))
        
                if board[nx][ny] == -1 and minV >= visited[nx][ny]: 
                    nextClient.append((nx,ny,visited[nx][ny]-1))
                    minV = visited[nx][ny]
    return nextClient

isPossible = True

def searchPathToDst(src,dest):
    deq = deque()
    deq.append(src)
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[src[0]][src[1]] = True

    while deq:
        px, py = deq.popleft()
        for nx, ny in [(px+1,py),(px,py+1),(px-1,py),(px,py-1)]:
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]==False and board[nx][ny]!=1:
                visited[nx][ny] = visited[px][py] + 1
                deq.append((nx,ny))
                if dest[0] == nx and dest[1] == ny:
                    return visited[nx][ny]-1
    return False


while len(client.keys()) > 0:
    nextClient = searchClient(taxi)
    nextClient.sort(key=lambda x: (x[0],x[1]))
    
    if len(nextClient) == 0:
        isPossible = False
        break
    
    board[nextClient[0][0]][nextClient[0][1]] = 0
    clientSrc = (nextClient[0][0],nextClient[0][1])
    clientDst =  client[clientSrc]
    gasToClient = nextClient[0][2]
    gasToDst = searchPathToDst(clientSrc,clientDst)
    if gasToDst==False:
        isPossible = False
        break
    taxi = clientDst

    del client[clientSrc]

    curGas -= (gasToClient+gasToDst)
    if curGas < 0:
        isPossible = False
        break
    curGas += gasToDst*2

if isPossible: 
    print(curGas)
else:
    print(-1)