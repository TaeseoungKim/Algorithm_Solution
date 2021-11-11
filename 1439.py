import sys
input= sys.stdin.readline

bit_list = list(map(int, input().strip()))
len = bit_list.__len__()
cnt = 0

for i in range(1,len):
    if bit_list[i] == bit_list[i-1]:
        continue
    else:
        cnt += 1

if cnt%2 == 0:
    print(cnt//2)
else:
    print(cnt//2 + 1) 