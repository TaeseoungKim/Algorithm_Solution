import sys
from collections import deque
input = sys.stdin.readline

STR = input().rstrip()
answ=[]
deq=deque()
isTag=False

for i in range(len(STR)):
    if STR[i]=='<':
        while deq:
            answ.append(deq.pop())
        answ.append(STR[i])
        isTag=True
        continue
    elif STR[i]=='>':
        answ.append(STR[i])
        isTag=False
        continue
    
    if not isTag and STR[i]==' ':
        while deq:
            answ.append(deq.pop())
        answ.append(' ')
        continue

    if isTag:
        answ.append(STR[i])
    else:
        deq.append(STR[i])
while deq:
        answ.append(deq.pop())
print(*answ,sep='')