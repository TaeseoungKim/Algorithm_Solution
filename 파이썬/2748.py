from collections import deque

n = int(input())
deq = deque()

for i in range(n+1):
    if i == 0:
        deq.append(0)
    elif i == 1:
        deq.append(1)
    else:
        deq.append(deq[i-1] + deq[i-2])
print(deq[n])