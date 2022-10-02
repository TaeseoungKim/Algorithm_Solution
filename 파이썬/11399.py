import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
Result_list = [ 0 for _ in range(N) ]
N_list = sorted(N_list)
Result=0
for i in range(N):
    for j in range(i+1):
        Result_list[i] += N_list[j]
for i in range(N):
    Result += Result_list[i]
print(Result)