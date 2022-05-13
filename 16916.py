import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
print(1 if str1.find(str2)!=-1 else 0)