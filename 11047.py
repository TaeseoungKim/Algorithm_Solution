import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin_list = [ int(input()) for _ in range(N)]
coin_index = N-1
result = 0
while(True):
    if K == 0:
        break
    elif K - coin_list[coin_index] < 0: # 뺄 수 없을 때 
        coin_index -= 1               # coin_index를 -1하고 continue
        continue
    else: # 뺄 수 있을 때
        quotient = K//coin_list[coin_index] # 남은 값을 동전으로 나눈 몫
        result += quotient
        K -= quotient * coin_list[coin_index]
        coin_index -= 1
        continue

print(result)