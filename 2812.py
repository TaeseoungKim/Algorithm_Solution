import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = input().rstrip()

answ = []
maxValue = 0
idx = -1
for i in range(1,n-k+1):
    for d in range(idx+1,k+i):
        cur = int(num[d])
        if cur>maxValue:
            maxValue=cur
            idx=d
    answ.append(maxValue)
    maxValue=0
print(*answ,sep="")