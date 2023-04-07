

def test1(board):

    board[3][3] = 10000


def test2():
    visited = [[False for _ in range(10)] for _ in range(10)]
    test1(visited)
    for i in range(10):
        print(visited[i])


test2()
