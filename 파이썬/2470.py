import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

left = 0
right = N-1
result = N_list[left] + N_list[right]
tmp_left = left
tmp_right = right

while left < right:
    check = N_list[left] + N_list[right]
    if abs(check) < abs(result):
        result = check
        tmp_left = left
        tmp_right = right
        if result == 0:
            break
    if check < 0:
        left += 1
    else:
        right -= 1

print(N_list[tmp_left], N_list[tmp_right])

    