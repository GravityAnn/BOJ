import sys
input = sys.stdin.readline
from collections import deque
a, b = map(int, input().split())

#2곱하기
#1을 수의 가장 오른쪽에 추가
#만들 수 없으면 -1 출력

queue = deque()
# print(visited)

def dfs():
    queue.append((b, 1))
    while(queue):
        var1, cnt = queue.pop()
        # print("var1",var1)

        if(var1 == a):
            print(cnt)
            break

        if(var1 % 10 == 1 ) and (var1 // 10 >= a):
            var2 = var1 //10
            queue.append((var2, cnt+1))

        elif(var1%2 == 0) and (var1 //2 >= a):
            var2 = var1 //2
            queue.append((var2, cnt+1))

        else:
            print(-1)
            break
dfs()
