import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
N_list = list( map(int, input().split()))

max_1 = max(N_list)
index = N_list.index(max_1)
N_list.pop(index)

max_2 = max(N_list)
cnt_k = 0
result = 0

for _ in range(M):
    
    if cnt_k == K:
        cnt_k = 0
        result += max_2
    else:
        result += max_1
        cnt_k += 1

print(result)
    
    

