import sys

n = int(sys.stdin.readline())
t = [0] * n
p = [0] * n 
dp = [0] * (n+1)

# M은 이전에 저장된 M의 값과 dp[i]중 큰 것으로 갱신한다 
# dp[i]는 '현재까지의 수익에 이번 상담의 수익을 더한 값'과 '오늘의 상담이 끝나는 시점의 수익' 중 큰 값을 저장한다

for _ in range(n):
    t[_], p[_] = map(int,sys.stdin.readline().split())

M = 0
for i in range(n):
    M = max( dp[i] , M )
    if t[i] + i > n :
        continue
    dp[ i + t[i] ] = max(M + p[i] , dp[ i + t[i] ]) # 지금꺼 적용할 때 VS 원래거


print(max(dp))