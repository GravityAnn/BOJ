import sys
from collections import deque
input = sys.stdin.readline

# n, m = map(int, input().split()) #세로, 가로
#가장 왼쪽 아래 칸에 위치해있다.
#방문한 칸이 5개 이상이라면 이동 방법을 모두 한 번씩 사용해야 한다.

n = int(input())#n장의 카드
#제일 마지막에 남는 카드
#123456
#맨윗장 버리기 -> 맨 윗장 맨뒤로
#23456 -> 34562
#4562 -> 5624
#624 -> 246
#46 -> 64
#4 -> 4
queue = deque()
for i in range(1, n+1):
    queue.append(i)
    # print(i)
# print(queue)
var1 = 0
while(queue):
    var1 = queue.popleft()
    if( not queue):
        break
    tmp = queue.popleft()
    queue.append(tmp)
print(var1)








