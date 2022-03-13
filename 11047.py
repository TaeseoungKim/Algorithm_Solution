from collections import deque
n,k = map(int, input().split())
coins = deque()
for _ in range(n):
    coins.append(int(input()))
cnt = 0
while k!=0:
    cur = coins.pop()
    qu = k//cur

    if qu>=1:
        cnt+=qu
        k-=cur*qu
        
print(cnt)            