import sys
import copy
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))
max_num, min_num = -10e10, 10e10

def check(copied_op,cur):
    global max_num, min_num
    if sum(copied_op) == 0:
        max_num = max(max_num, cur)
        min_num = min(min_num, cur)


def op_bfs(idx, opcode_list, cur):
    global max_num, min_num
    
    
    if opcode_list[0] != 0:
        copied_op = copy.deepcopy(opcode_list)
        copied_op[0] -= 1
        tmp_cur = cur+num_list[idx]
        op_bfs(idx+1,copied_op,tmp_cur)
        check(copied_op,tmp_cur)
        
    if opcode_list[1] != 0:
        copied_op = copy.deepcopy(opcode_list)
        copied_op[1] -= 1
        tmp_cur = cur-num_list[idx]
        op_bfs(idx+1,copied_op,tmp_cur)
        check(copied_op,tmp_cur)

    if opcode_list[2] != 0:
        copied_op = copy.deepcopy(opcode_list)
        copied_op[2] -= 1
        tmp_cur = cur*num_list[idx]
        op_bfs(idx+1,copied_op,tmp_cur)
        check(copied_op,tmp_cur)

    if opcode_list[3] != 0:
        copied_op = copy.deepcopy(opcode_list)
        copied_op[3] -= 1
        if cur < 0:
            cur = abs(cur)
            tmp_cur = -1*(cur//num_list[idx])
        else:
            tmp_cur = cur//num_list[idx]
        op_bfs(idx+1,copied_op,tmp_cur)
        check(copied_op,tmp_cur)

    return

op_bfs(1,op_list,num_list[0])
print(max_num)
print(min_num)