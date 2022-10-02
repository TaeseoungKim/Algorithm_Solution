N, L = map(int, input().split())
L = str(L)
curNum = 1
cnt = 0
while cnt!=N:
    if L in str(curNum):
        curNum+=1
        continue
    curNum+=1
    cnt += 1
print(curNum-1)