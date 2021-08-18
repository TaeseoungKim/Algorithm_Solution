n = int(input())
list = list(map(int, input().split()))
sum = [ 0 for _ in range(n) ]

for i in range(n):
    tmp_sum = 0
    for d in range(i,n):
        tmp_sum = 0
        for x in range(i,d,1):
            tmp_sum += list[x]
        if tmp_sum > sum[i]:
            sum[i] = tmp_sum

print(max(sum))