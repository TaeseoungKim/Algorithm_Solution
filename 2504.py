import sys
from collections import deque
input = sys.stdin.readline
inStr = input()
deq = deque()
# 재귀함수로 푸는게 날듯하다
lev = 0
lev_sum = []
for c in inStr:
    if c == '(':
        lev += 1
        if len(lev_sum)!=lev:
            lev_sum.append([])
        deq.append(2)
    if c == ')':
        lev -= 1
        if  deq.pop() == 2:
            lev_sum = sum(lev_sum[lev])