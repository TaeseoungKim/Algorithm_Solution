import copy

n, k = map(int, input().split())
list_tmp = []


for i in range(n):
    str_in = input()
    list_tmp.extend(str_in.split())

list_tmp = list(map(int, list_tmp))
s, x, y = map(int, input().split())

array = [[list_tmp[a*n + b] for b in range(n)] for a in range(n)]
array_tmp = copy.deepcopy(array)

for i in range(s):
    
    for a in range(n):
        for b in range(n):

            if array[a][b] == 0:
                continue

            if a-1 >= 0:
                if array[a-1][b] != 0 :
                    pass
                elif array_tmp[a-1][b] > array[a][b] :
                    array_tmp[a-1][b] = array[a][b]
                elif array_tmp[a-1][b] == 0 :  # 다른 방법이 있는지
                    array_tmp[a-1][b] = array[a][b]

                

            if a+1 < k:
                if array[a+1][b] != 0 :
                    pass
                elif array_tmp[a+1][b] > array[a][b] :
                    array_tmp[a+1][b] = array[a][b]
                elif array_tmp[a+1][b] == 0 : 
                    array_tmp[a+1][b] = array[a][b]

            if b-1 >= 0:
                if array[a][b-1] != 0 :
                    pass
                elif array_tmp[a][b-1] > array[a][b] : 
                    array_tmp[a][b-1] = array[a][b]
                elif array_tmp[a][b-1] == 0 : 
                    array_tmp[a][b-1] = array[a][b]
           
            if b+1 < k:
                if array[a][b+1] != 0 :
                    pass
                elif array_tmp[a][b+1] > array[a][b] :
                    array_tmp[a][b+1] = array[a][b]
                elif array_tmp[a][b+1] == 0 : 
                    array_tmp[a][b+1] = array[a][b]
    
    array = copy.deepcopy(array_tmp)

array = array_tmp

print(array[x-1][y-1])