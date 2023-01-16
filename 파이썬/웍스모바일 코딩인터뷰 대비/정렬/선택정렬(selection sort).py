import sys
# 시간복잡도 BIG O : n^2
board = [4, 6, 1, 3, 5, 2]


def selectionSort(arr):
    for i in range(len(arr)-1):
        idx_min = i
        for d in range(i+1, len(arr)):
            if arr[idx_min] > arr[d]:
                idx_min = d
        arr[i], arr[idx_min] = arr[idx_min], arr[i]

    return arr


board = selectionSort(board)
print(board)
