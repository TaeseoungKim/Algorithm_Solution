N, L = map(int, input().split())
curNum = 1
curLabel = 1

while True:
    if str(curLabel).find(str(L)) != -1:
        curLabel += 1
        continue
    else:
        curNum += 1
        if N+1 == curNum:
            break
        curLabel += 1

print(curLabel)
