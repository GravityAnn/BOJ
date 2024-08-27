#2583
import sys
input = sys.stdin.readline
'''
sys.setrecursionlimit(10**6)
m, n, k = map(int, input().split()) #가로, 세로, 직사각형 개수
graph = [[1]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1,x2):
        for i in range(y1, y2):
            graph[i][j] = 0

cnt = 0

def dfs(x, y):
    global result
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0
    else:
        if graph[x][y] == 1: #뭔가 들어있으면;
            result += 1
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return 0
        return 0

ans = []
result = 0
cnt =0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            if result != 0:
                ans.append(result)
                result = 0


print(len(ans))
ans.sort()
for i in ans:
    print(i, end=" ")

print(sys.getrecursionlimit())

dfs로는 python이 정한 최대 재귀 깊이보다 나의 코드상의 재귀의 깊이가 더 깊어 재귀에러가 발생한다고 한다. 
따라 이문제는 dfs 방식이 적합하지 않다. 
'''
from collections import deque

m, n, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global ans
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    size = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')



