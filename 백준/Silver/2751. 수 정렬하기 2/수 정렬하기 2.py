import sys
from collections import deque
input = sys.stdin.readline




# n, m = map(int, input().split()) #세로, 가로

n = int(input())

a = [int(input()) for _ in range(n)]
a.sort()
for i in a:
    print(i)







