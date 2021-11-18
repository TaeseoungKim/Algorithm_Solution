import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [ input() for _ in range(N) ]
M_list = [ input() for _ in range(M) ]

result = set(N_list) & set(M_list)

print(len(result))
for _ in sorted(result):
    print(_,end='')