
W = input()
K = int(input())
W_len = len(W)
board = [[0]*W_len for _ in range(W_len)]
alphaCnt = dict()

for i in range(W_len):
    if alphaCnt[W[i]]:
        alphaCnt[W[i]] = alphaCnt[W[i]]+1

    else: alphaCnt[W[i]]=1
    
