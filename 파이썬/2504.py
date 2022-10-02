import sys
from collections import deque
input = sys.stdin.readline
inStr = input()

deq = deque()
tmp=1
answer = 0
for i in range(len(inStr)-1):
    if inStr[i]=='(':
        tmp *=2
        deq.append(inStr[i])
    elif inStr[i]=='[':
        tmp *=3
        deq.append(inStr[i])
    elif inStr[i]==')':
        if not deq or deq[-1]=='[':
            answer=0
            break
        if inStr[i-1]=='(':
            answer += tmp       
        tmp //=2
        deq.pop()
    elif inStr[i]==']':
        if not deq or deq[-1]=='(':
            answer=0
            break
        if inStr[i-1]=='[':
            answer += tmp       
        tmp //=3
        deq.pop()


if deq:
    print(0)
else:
    print(answer)