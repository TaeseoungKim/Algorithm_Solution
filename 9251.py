import sys
input = sys.stdin.readline
str1 = list(input().strip())
str2 = list(input().strip())
len1 = len(str1)
len2 = len(str2)
dp = [[0]*len2 for _ in range(len1)]
for i in range(len1):
    for d in range(len2):
        if str1[i]==str2[d]:
            dp[i][d] = max(dp[i][d]+1, )
    