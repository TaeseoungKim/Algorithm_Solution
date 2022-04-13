from collections import deque
import sys
input = sys.stdin.readline

# 2 25 25 25 25
# 동서남북
n, a, b, c, d = map(int, input().split())
a = -1 if a!=0 else 0
b = 1 if b!=0 else 0
c = -1 if c!=0 else 0
d = 1 if d!=0 else 0
print("엥",a,b,c,d)
# x축, y축
board = []
cur = (0,0)
visit = dict()

allCNT = 0
falseCNT = 0

def dfs(cur_x,cur_y,visit,cnt):
    global allCNT,falseCNT
    allcnt, falsecnt = 0,0
    if cnt==n:
        return
    visit[(cur_x,cur_y)]=1
    
    for next_x, next_y in [(cur_x,cur_y+a),(cur_x,cur_y+b),(cur_x+c,cur_y),(cur_x+d,cur_y)]:
        if cur_x == next_x and cur_y == next_y:
            print("원")
            continue
        if visit.get((next_x,next_y))==None:
            print("투")
            dfs(next_x,next_y,dict(visit),cnt+1)
        else:
            falsecnt += 1
        allCNT+=1
        if allCNT==n:
            return

dfs(visit)
print("음",falseCNT,allCNT)
if allCNT==0:
    print("뭐여시벌")
else:
    print(falseCNT/allCNT)


