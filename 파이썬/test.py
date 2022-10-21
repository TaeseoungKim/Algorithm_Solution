sortedArr = [[2, 3], [1, 3], [1, 2], [1, 4], [1, 1], [1, 5]]
sortedArr = sorted(sortedArr, key=lambda x: (x[0], x[1]))

print(sortedArr)
