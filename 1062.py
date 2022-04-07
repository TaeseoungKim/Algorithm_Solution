import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(input().strip())

print(board)
if k<5:
    print(0)
else:
    k-=5
    dic = dict({'a':1,'n':1,'t':1,'c':1,'i':1})
    for word in board:
        print("1:",word)
        print(word[4:-4])
        for idx, c in enumerate(word[4:-4]):

        
    
