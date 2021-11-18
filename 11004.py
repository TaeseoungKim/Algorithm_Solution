import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N_list = sorted(list( map(int, input().split())))
print(N_list[K-1])