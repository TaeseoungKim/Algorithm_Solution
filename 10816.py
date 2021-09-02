import sys

#로직에선 쓰이지 않기 때문애 _ 변수에 담아준다.
#sorted()는 리스트를 반환하기 때문에 list()함수를 따로 사용해주지 않아도 된다.
_ = int(input()) 
N = sorted(map(int, sys.stdin.readline().split()))

#dictionary 생성
N_dict = {}

#중복되는 카드들을 dictionary에 저장.
for i in N:
    if i not in N_dict:
        N_dict[i] = 1
    else:
        N_dict[i] += 1

_ = int(input())
M = list(map(int, sys.stdin.readline().split()))

for i in M:
    print(N_dict[i] if N_dict.get(i) else "0",end=" ")
