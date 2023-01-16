# O(NlogN), worst case O(n^2)

# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# arr = arr1+arr2
# print(arr) => [1,2,3,4,5,6] 임을 이용한다.

board = [8, 13, 2, 6, 1, 4]


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    leftSide = [x for x in tail if x < pivot]
    rightSide = [x for x in tail if x >= pivot]

    return quickSort(leftSide) + [pivot] + quickSort(rightSide)


board = quickSort(board)
print(board)
