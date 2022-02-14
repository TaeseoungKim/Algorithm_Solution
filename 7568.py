import sys
input = sys.stdin.readline

n = int(input())
people = []
rank = [0]*n
h, w = (0,0)    

for _ in range(n):
    h, w = map(int, input().split())
    people.append((h,w))

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
    rank[i] += 1

print(*rank)