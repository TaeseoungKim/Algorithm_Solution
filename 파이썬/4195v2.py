import sys
input = sys.stdin.readline

def find(name):
    if parent[name] != name:
        parent[name] = find(parent[name])
    return parent[name]


def union(friendA, friendB):
    parentA = find(friendA)
    parentB = find(friendB)

    if parentA!=parentB:
        parent[parentB] = parentA
        nums[parentA] += nums[parentB]
    print(nums[parentA])

TestCase = int(input())
for _ in range(TestCase):
    F = int(input())
    parent, nums = {}, {}
    
    for f in range(F):
        friendA, friendB = input().strip().split()
        if not friendA in parent:
            parent[friendA] = friendA
            nums[friendA]=1
        if not friendB in parent:
            parent[friendB] = friendB
            nums[friendB]=1
        union(friendA,friendB)
            