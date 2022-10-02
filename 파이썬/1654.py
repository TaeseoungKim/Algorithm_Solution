import sys

K , N = map(int, input().split())
length = [int(sys.stdin.readline()) for _ in range(K)]

# 초기값 설정
left, right = 1,max(length)

while left <= right :

    middle = (left+right)//2
    quotient_sum = 0

    for i in length:
        quotient_sum += i // middle

    if quotient_sum >= N :
        left = middle+1
    else:
        right = middle-1

print(right)