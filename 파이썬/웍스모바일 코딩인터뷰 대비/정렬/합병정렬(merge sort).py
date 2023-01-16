# 쪼개지는 과정 : logN
# 비교하는 과정 : N
# O(NlogN)

board = [6, 2, 4, 1, 3, 7, 5, 8]


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] > rightArr[j]:
                arr[k] = rightArr[j]
                j += 1
                k += 1
            else:
                arr[k] = leftArr[i]
                i += 1
                k += 1
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


mergeSort(board)
print(board)
