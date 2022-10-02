import sys
input = sys.stdin.readline

input_str = input().strip()
n = int(input())
leng_str = len(input_str)
print(input_str)
print(n)
result = 0
for i in range(n):
    print(input_str[i],"!?",input_str[leng_str-n+i])
    if input_str[i] != input_str[leng_str-n+i]:
        result += 1
        print("다르다 !!")

print(result)
