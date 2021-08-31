
n = int(input())
find_n = int(input())

tmp = n - (n - 1) // 2


array = [[0 for col in range(n)] for row in range(n)]

array[tmp-1][tmp-1] = 1 #
cur_number = 2

row = tmp-1
column = tmp-1

for i in range(1,tmp,1):
    
    row -= 1
    array[row][column] = cur_number
    cur_number += 1

    for a in range(i*2-1):
        column +=1
        array[row][column] = cur_number
        cur_number += 1

    for a in range(i*2):
        row += 1
        array[row][column] = cur_number
        cur_number += 1

    for a in range(i*2):
        column -= 1
        array[row][column] = cur_number
        cur_number += 1

    for a in range(i*2):
        row -= 1
        array[row][column] = cur_number
        cur_number += 1

for i in range (n):
    for a in range (n) :
        if( find_n == array[i][a] ):
            row=i+1
            column=a+1
        print(array[i][a],end=" ")
    print("")
print(row,column)






