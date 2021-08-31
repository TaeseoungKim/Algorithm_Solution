n = int(input())
list = list(map(int,input().split()))

#3중 for문...
for i in range(1,n):
    list[i] = max(list[i] , list[i-1] + list[i])

print(list)
print(max(list))