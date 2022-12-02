# 삽입 정렬은 한마디로 표현하면 정렬 범위를 1칸씩 확장해나가면서
# 새롭게 정렬 범위에 들어온 값을 기존 값들과 비교하여 알맞은 자리에 꼽아주는 알고리즘입니다.
# O(n^2)
board = [4, 6, 1, 3, 5, 2]


def insertionSort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


board = insertionSort(board)
print(board)
