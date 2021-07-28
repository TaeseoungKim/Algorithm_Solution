board = [ [ 1,2,3,4,5] , [2,3,5,50,20] ]


t_max = []
for _ in range(2):
    t_max.append(max(board[_]))
    
max_height = max(t_max)
print(max_height)