# 실제 시간 복잡도는 (n-1)^2임에 유의한다.

board = [6, 5, 3, 1]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for d in range(n-1):
            if arr[d] > arr[d+1]:
                arr[d], arr[d+1] = arr[d+1], arr[d]
    return arr


board = bubbleSort(board)
print(board)
