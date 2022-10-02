import sys
input = sys.stdin.readline

words = []
n = int(input())
result = 0

for _ in range(n):
    c_set = set()
    word = input()
    result += 1
    for i in range(len(word)):
        if i == 0:
            c_set.add(word[i])
            continue
        if word[i] != word[i-1]:
            if word[i] in c_set:
                result -= 1
                break
            else:
                c_set.add(word[i])
            
print(result)