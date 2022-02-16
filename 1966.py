import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, seq = map(int, input().split())
    deq = deque((map(int, input().split())))
    cnt = 0
    while(True):
        cnt += 1
        popped = deq.popleft()
        seq -= 1

        if (seq == -1) or (not deq):
            print("result",cnt)
            break
        elif max(deq) > popped:
            if seq == -1:
                seq += len(deq)+1
            deq.append(popped)
            cnt -= 1
        
    