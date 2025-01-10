import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) #세로 가로
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False ]*m for _ in range(n)]
#그림의 개수, 가장 큰 그림의 넓이 출력
#1로 연결된 것이 한그림
#넓이 : 1의 개수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    cnt = 0
    queue = deque()
    queue.append([x, y])
    visit[x][y] = True
    cnt += 1
    while (queue):
        x, y = queue.popleft()
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < n) and (0<= ny < m) and (graph[nx][ny] == 1) and (visit[nx][ny] == False):
                queue.append([nx, ny])
                visit[nx][ny] = True
                cnt += 1
    return cnt


count = 0
max_ans = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1) and (visit[i][j] == False):
            ans = BFS(i, j)
            count += 1
            if(max_ans < ans):
                max_ans = ans
print(count)
print(max_ans)


