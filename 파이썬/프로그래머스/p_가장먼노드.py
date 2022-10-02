from collections import deque

def solution(n, edge):
    board = [[] for _ in range(n+1)]
    minPath = [0]*(n+1)
    #dfs 구현
    for x,y in edge:
        board[x].append(y)
        board[y].append(x)

    deq = deque()
    deq.append(1)
    while deq:
        cur = deq.popleft()
        for next in board[cur]:
            if next!=1 and minPath[next]==0:
                minPath[next] = minPath[cur]+1
                deq.append(next)
    
    maxV = max(minPath)
    answer=0
    for path in minPath:
        if maxV==path:
            answer+=1
    return answer



n=6
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)