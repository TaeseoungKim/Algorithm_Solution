n = int(input())
list = list(map(int,input().split()))

for i in range(1,n):
    list[i] = max(list[i] , list[i-1] + list[i] )

print(list)
print(max(list))