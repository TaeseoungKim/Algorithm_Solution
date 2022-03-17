# https://suri78.tistory.com/11 엑셀표 참고
# https://myjamong.tistory.com/317 풀이 참고
import sys
input = sys.stdin.readline
str1 = list(input().strip())
str2 = list(input().strip())
len1 = len(str1)
len2 = len(str2)
dp = [[0]*(len1+1) for _ in range(len2+1)]

for i in range(1,len2+1):
    for d in range(1,len1+1):
        char1 = str1[d-1]
        char2 = str2[i-1]
        if char1==char2:
            dp[i][d] = dp[i-1][d-1]+1
        else:
            dp[i][d] = max(dp[i-1][d],dp[i][d-1])
print(dp[len2][len1])