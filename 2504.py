import sys
from collections import deque
input = sys.stdin.readline
inStr = input()
deq = deque()
cal = []
result = 0
v=0
# 재귀함수로 푸는게 날듯하다
def cal(grade):
    tmp = 0
    for i in range(len(cal)):
        if i==0: tmp += cal[i]
        else: tmp *= cal[i]
    result += tmp
    cal = []
#(()[[]])([])

for c in inStr:
    deq.append(c)
    if c == ')':
        if deq.pop() == '(':
            break
    elif c == ']':
        if deq.pop() == '[':
            break
print(result)