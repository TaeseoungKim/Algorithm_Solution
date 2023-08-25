import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
print("board",board)
visited = [ 0 for i in range(N)]

# 정렬을 하고 이분 탐색
# 소팅을 ... ... ... ... 
for i in range(N):
    if i == 0:
        visited[i] = 1
        continue

    prevMax = max(board[:i])
    maxIdx = board.index(prevMax,0,i)
    visited[i] = visited[maxIdx]+1
print(max(visited)