import sys
input = sys.stdin.readline
from collections import deque

k = int(input())#정수
stack = deque()
# 0~ 1000000사이 값
#0일 경우 최근 수를 지우고, 아닐 경우 해당 수를 씀
#0일 경우 스택가 비어있지 않음
#그 수의 합을 구하여라
for i in range(k):
    num = int(input())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
