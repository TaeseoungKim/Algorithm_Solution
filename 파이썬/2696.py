# 23
# 23 41 13 22 -3 24 -31 -11 -8 -7
# 3 5 103 211 -311 -45 -67 -73 -81 -99
# -33 24 56

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 10:
        board = list(map(int, input().split()))
    else: 
        board = list(map(int, input().split()))
        rem = n//10
        if rem*10<n:
            for _ in range(rem):
                board.extend(list(map(int, input().split())))
        else:
            for _ in range(rem-1):
                board.extend(list(map(int, input().split())))

    tmp = []
    ans = []
    mid = 0
    cnt = 0
    for num in board:
        cnt += 1
        tmp.append(num)
        if cnt%2!=0:
            tmp.sort()
            ans.append(tmp[mid])
            mid+=1
    if n <= 10:
        print(*ans)
    else: 
        rem = n//10
        if rem*10<n:
            for z in range(rem+1):
                if z==rem+1: print(*ans[z*10:z*10+10],end="")
                else: print(*ans[z*10:z*10+10])
        else:
            for z in range(rem):
                if z==rem: print(*ans[z*10:z*10+10],end="")
                else: print(*ans[z*10:z*10+10])
        

            
            
