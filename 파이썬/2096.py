import sys
input = sys.stdin.readline

N = int(input())

one, two, three = map(int, input().split(" "))
Max_dp = [one, two, three]
Min_dp = [one, two, three]

Max_dp[0], Max_dp[1], Max_dp[2] = one, two, three
Min_dp[0], Min_dp[1], Min_dp[2] = one, two, three

for i in range(1, N):
    one, two, three = map(int, input().split(" "))
    TmpMax_dp = [0, 0, 0]
    TmpMin_dp = [0, 0, 0]

    TmpMax_dp[0] = one+max(Max_dp[0], Max_dp[1])
    TmpMin_dp[0] = one+min(Min_dp[0], Min_dp[1])

    TmpMax_dp[1] = two+max(Max_dp[0], Max_dp[1], Max_dp[2])
    TmpMin_dp[1] = two+min(Min_dp[0], Min_dp[1], Min_dp[2])

    TmpMax_dp[2] = three+max(Max_dp[1], Max_dp[2])
    TmpMin_dp[2] = three+min(Min_dp[1], Min_dp[2])

    Max_dp[0], Max_dp[1], Max_dp[2] = TmpMax_dp[0], TmpMax_dp[1], TmpMax_dp[2]
    Min_dp[0], Min_dp[1], Min_dp[2] = TmpMin_dp[0], TmpMin_dp[1], TmpMin_dp[2]

print(max(Max_dp), min(Min_dp))
