import sys
input = sys.stdin.readline
from collections import deque

n = int(input())#정수
stack = deque()
# 0~ 1000000사이 값
#0일 경우 최근 수를 지우고, 아닐 경우 해당 수를 씀
#0일 경우 스택가 비어있지 않음
#그 수의 합을 구하여라
for i in range(n):
    num1 = list(map(int, input().split()))
    if(num1[0] == 1):
        stack.append(num1[1])
    elif(num1[0] == 2):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(num1[0] == 3):
        print(len(stack))
    elif(num1[0] == 4):
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(num1[0] == 5):
        if (len(stack) == 0):
            print(-1)
        else:
            num = stack.pop()
            print(num)
            stack.append(num)
