#우선, 1만 써서 합을 나타내는 방법 1가지씩은 모두 가지고 있으므로 dp 테이블을 1로 초기화해준다. 
#그리고 2가 추가되는 경우dp[i] = dp[i] + dp[i - 2]와 3이 추가되는 경우dp[i] = dp[i] + dp[i - 3]를 한번씩 더 갱신해주면 된다.
dp = [1]*10001
for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]
t = int(input())
for _ in range(t):
    v = int(input())
    print(dp[v])