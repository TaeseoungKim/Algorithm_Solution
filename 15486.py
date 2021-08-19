import sys
n = int(sys.stdin.readline())
t = []
p = []
dp = [ 0 for _ in range(n+1) ]

for _ in range(n):
    tmp_t, tmp_p = map(int , sys.stdin.readline().split())
    t.append(tmp_t)
    p.append(tmp_p)

M = 0
for i in range(n):
    M = max(dp[i],M)
    if t[i] + i > n:
        continue
    # 지금꺼 적용할 때 vs 원래거
    dp[i+t[i]] = max(M + p[i] , dp[i + t[i]] )

print(max(dp))
