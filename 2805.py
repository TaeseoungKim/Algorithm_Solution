# 이분탐색 알고리즘이지만, 주어진 높이에 이분탐색을 해주는 것이 아닌,
# 주어진 (0 ~ 나무 높이 최대값)에서 이분 탐색을 해준다.

N , M = map(int, input().split())
height = list(map(int, input().split()))

def cal(data):

    if data > middle:
        return data - middle
    else:
        return 0
    
# 초기값 설정
left = 0
right = max(height)
middle = (left+right)//2

while(True):
    cut_sum = sum(map(cal,height))

    
    if cut_sum == M :
        print(middle)
        exit()

    elif cut_sum < M :
        right = middle-1
        middle = (left+right)//2
        continue

    else :
        left = middle+1
        middle = (left+right)//2
        continue