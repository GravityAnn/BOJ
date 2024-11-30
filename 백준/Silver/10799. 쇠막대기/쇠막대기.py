import sys
input = sys.stdin.readline
from collections import deque

list1 = list(input())
ans = 0
queue = deque()
# print(len(list1))
for i in range(len(list1)-1):
    # print(queue)
    if(list1[i] == '('):
        queue.append('(')
    else:
        queue.pop()
        if(list1[i-1] == '('):
            ans += queue.count('(')
            # print("!!!count!!! : ", ans)
        else:
            ans += 1

print(ans)

