from sys import stdin
 
 
def solution(queries, stack):
    #5. MAX값 정하기
    MAXVAL = 10 ** 9
    for query in queries:
        # 6. try..except로 처리.
        # except에는 오류를 구체화할 수 있지만
        # 아무것도 안 줄 경우 모든 에러를 받아줌.
        # raise는 에러를 강제로 발생시키는 코드
        # 연산이 다 끝났을 때 값이 1개가 아니거나
        # 연산 결과 최대값을 넘어가면 에러이다. 0으로 나누는 경우도
        # 최대값을 넘기는 에러에 포함이 된다.
        # 결과는 항상 stack[-1]을 참조하면 된다.
 
        try:
            if query.startswith('NUM'):
                stack.append(int(query.replace('NUM ', '')))
            else:
                if query == 'POP':
                    stack.pop()
                elif query == 'INV':
                    stack.append(-stack.pop())
                elif query == 'DUP':
                    stack.append(stack[-1])
                elif query == 'SWP':
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                elif query == 'ADD':
                    stack.append(stack.pop() + stack.pop())
                elif query == 'SUB':
                    f, s = stack.pop(), stack.pop()
                    stack.append(s - f)
                elif query == 'MUL':
                    stack.append(stack.pop() * stack.pop())
                elif query == 'DIV':
                    f, s = stack.pop(), stack.pop()
                    # 두 수중 한 수가 음수일 때는 음수 몫을 저장
                    r = abs(s) // abs(f)
                    if (0 < f and s < 0) or (f < 0 and 0 < s):
                        r = -r
                    stack.append(r)
                elif query == 'MOD':
                    f, s = stack.pop(), stack.pop()
                    r = abs(s) % abs(f)
                    if s < 0:
                        r = -r
                    stack.append(r)
            if stack and MAXVAL < abs(stack[-1]):
                raise
        except:
            return 'ERROR'
 
    if len(stack) != 1:
        return 'ERROR'
    return stack[0]
 
 
while True:
    #1. queries: 입력 한 세트이다.
    queries = [stdin.readline().strip()]
    if queries[0] == 'QUIT':
        break
 
    while True:
        #2. END가 나올 때 까지 명령어를 리스트에 저장
        if queries[-1] == 'END':
            break
        query = stdin.readline().strip()
        queries.append(query)
 
    #3. 시작값을 받고, queries와 초기스택을 넣어서 함수를 실행
    for _ in range(int(stdin.readline())):
        val = int(stdin.readline())
        print(solution(queries, [val]))
 
    #4. queries 중간 중간에 있는 공백 제거
    stdin.readline().strip()