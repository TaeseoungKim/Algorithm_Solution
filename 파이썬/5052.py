import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 입력
    N = int(input())
    N_list = [];
    # 일관성 검사를 위한 변수
    consistency = True
    
    # 리스트 입력
    for n in range(N):
        N_list.append(input())
    N_list.sort(key=len) # 정렬
    
    # 불안한 2중 for문...
    # 길이별로 정렬된 문자열들을 차례로 나머지들을 검사한다
    for i in range(N-1):
        i_len = len(N_list[i])-1
        
        for d in range(i+1,N):
            if N_list[i][0:i_len] == N_list[d][0:i_len]:
                consistency = False
                
    print("NO" if consistency==False else "YES")
    