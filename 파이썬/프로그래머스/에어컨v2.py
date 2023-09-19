import sys

temperature = 28
t1 = 18
t2 = 26
a = 10
b = 8
onboard	= [0, 0, 1, 1, 1, 1, 1]



def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10

    N = len(onboard)
    dp = [[sys.maxsize for i in range(51)] for _ in range(N)]
    dp[0][temperature] = 0

    for i in range(1, N): #0분일 때의 소비전력은 실외온도에 한해서 0일거임.
        start = 0
        end = 0
        if onboard[i]:
            start = t1
            end = t2
        else:
            start = min(t1, temperature)
            end = max(t2, temperature)
        
        for j in range(start, end + 1):
            if temperature < j:
                if 0 <= j-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+a)
                if j+1 <= 50:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
            elif temperature > j:
                if 0 <= j-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                if j+1 <= 50:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1]+a)
            elif temperature == j:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if  temperature != j and 0 <= j-1:
                dp[i][j] = min(dp[i][j], dp[i-1][j]+b)
        
        
    return min(dp[i])
solution(temperature, t1, t2, a, b, onboard)