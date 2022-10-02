import sys
input = sys.stdin.readline

def opcode_bin(op):
    if op == "ADD": return "000000"
    if op == "ADDC": return "000010" 
    if op == "SUB": return "000100"
    if op == "SUBC": return "000110"
    if op == "MOV" : return "001000"
    if op == "MOVC": return "001010"
    if op == "AND": return "001100"
    if op == "ANDC": return "001110"
    if op == "OR": return "010000"
    if op == "ORC": return "010010"
    if op == "NOT": return "010100"
    if op == "MULT" : return "011000"
    if op == "MULTC": return "011010"
    if op == "LSFTL": return "011100"
    if op == "LSFTLC": return "011110"
    if op == "LSFTR": return "100000"
    if op == "LSFTRC": return "100010"
    if op == "ASFTR": return "100100"
    if op == "ASFTRC": return "100110"
    if op == "RL": return "101000"
    if op == "RLC": return "101010"
    if op == "RR": return "101100"
    if op == "RRC": return "101110"

def regtobin(num):
    tmp = str(bin(num))
    return '{0:03d}'.format(int(tmp[2:]))

def contobin(num):
    tmp = str(bin(num))
    return '{0:04d}'.format(int(tmp[2:]))

    
n = int(input())
board = [input().split() for _ in range(n)]
result = ["" for _ in range(n)]
for i in range(len(board)):
    result[i] += opcode_bin(board[i][0])
    result[i] += regtobin(int(board[i][1]))
    result[i] += regtobin(int(board[i][2]))
    if result[i][4]=='0':
        result[i] += regtobin(int(board[i][3]))+'0'
    else: result[i] += contobin(int(board[i][3]))
    print(result[i])
        