import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
for i in range(n):
    line1 = list(input())
    stack = deque()
    VPS = True
    for j in line1:
        if(j == '('):
            stack.append('(')
        elif(j == ')'):
            if(len(stack) != 0):
                stack.pop()
            else:
                VPS = False
                break

    if(len(stack) == 0) and (VPS == True):
        print('YES')
    else:
        print('NO')