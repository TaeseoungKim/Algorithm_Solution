from collections import deque
def bfs(v):
    deq = deque()
    deq.append(v)
    visit[v][0]=0
    visit[v][1]=1
    while deq:
        cur = deq.popleft()
        for dx in move:
            next = cur+dx if dx!=2 else cur*2
            if 0<=next<=100000:
                if visit[next][0]==-1 or visit[next][0]>visit[cur][0]+1:
                        deq.append(next)
                        visit[next][0]=visit[cur][0]+1 
                        visit[next][1]=visit[cur][1]
                elif visit[next][0]==visit[cur][0]+1:
                    visit[next][1]+=visit[cur][1]
 

n, k = map(int,input().split())
visit = [[-1,0] for _ in range(100001)] # (distance, cnt)
move = [1,-1,2]
bfs(n)
print(visit[k][0])
print(visit[k][1])