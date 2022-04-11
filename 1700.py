from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))
seq_len = len(seq)
consent = dict.fromkeys(seq,0)
print(consent)




def bfs(v):
    deq = deque()
    deq.append(v)
    
    for i in range(seq_len):

    return

bfs(0)