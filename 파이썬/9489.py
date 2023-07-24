import sys
input = sys.stdin.readline
# 증가하는 정수 수열을 이용해서 트리를 만드는 방법은 다음과 같다.

# 첫 번째 정수는 트리의 루트 노드이다.
# 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타낸다. 이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1보다 크다.
# 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 된다. 그러한 노드가 여러 가지 인 경우에는 가장 작은 수를 가지는 노드의 자식이 된다.
# 집합은 수가 연속하지 않는 곳에서 구분된다.
# 예를 들어, 수열 1 3 4 5 8 9 15 30 31 32를 위의 규칙을 이용해 트리를 만들면 아래 그림과 같이 된다.

# 1 3 4 5 8 9 15 30 31 32

# 1 (3, 4, 5) (8, 9) (15) (30, 31, 32)

# 트리를 만드는 로직,
# 형제를 찾는 로직

# 10 15
# 1 3 4 5 8 9 15 30 31 32

N, K = map(int, input().split())
board = list(map(int, input().split()))

tree = [[board[0], []]] # (value, children Node)

tempChildNodes = []

curNode = tree[0]

for i in range(1,len(board)):
    if not tempChildNodes:
        tempChildNodes.append(board[i])
    elif board[i] == board[i-1]+1:
        tempChildNodes.append(board[i])
    else: 
        curNode[1].append(tempChildNodes[:])
        tempChildNodes = []
        
    
    break