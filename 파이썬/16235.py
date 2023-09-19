from collections import deque
from copy import deepcopy

N, M, K = map(int, input().split())

feed = [[5 for _ in range(N)] for _ in range(N)]
originFeedStorage = [list(map(int, input().split())) for _ in range(N)]

tree = [[deque() for _ in range(N)] for _ in range(N)]





for i in range(M):
    x, y, old = map(int, input().split())
    tree[x-1][y-1].append(old)

for x in range(N):
    for y in range(N):
         sorted_list = sorted(list(tree[x][y]))
         print("sorted_list",sorted_list)
         tree[x][y] = deque(sorted_list)

for i in range(N):
     print(tree[i])
     
for year in range(K):

    nextFeedStorage = [[0 for _ in range(N)] for _ in range(N)]
    # 봄
    for x in range(N):
        for y in range(N):
            sorted_list = sorted(list(tree[x][y]))
            tree[x][y] = deque(sorted_list)
            for _ in range(len(tree[x][y])):
                old = tree[x][y].popleft()
                if feed[x][y] >= old:
                        tree[x][y].append(old+1)
                        feed[x][y] -= old
                        print("발동")
                else: 
                        nextFeedStorage[x][y] += old//2

    # 여름
    for x in range(N):
        for y in range(N):   
            feed[x][y] += nextFeedStorage[x][y]

    # 가을
    for x in range(N):
        for y in range(N):
            for _ in range(len(tree[x][y])):
                old = tree[x][y].popleft()
                if old % 5 == 0:
                    for nx, ny in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
                        if 0 <= nx < N and 0 <= ny < N:
                                tree[x][y].appendleft(1)
                tree[x][y].append(old)
    
    for x in range(N):
        for y in range(N):
            feed[x][y] += originFeedStorage[x][y]
    
answer = 0
for x in range(N):
    for y in range(N):
         answer += len(tree[x][y])
print(answer)
         