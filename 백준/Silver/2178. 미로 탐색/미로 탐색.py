# import sys
# input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# visited = [[False] * m for _ in range(n)]
#1은 이동 가능, 0은 이동 불가능, (n,m)까지 이동 가능한 최소 칸 수를 구하기
#시작과 도착 위치도 포함
INF = int(1e9)
graph = []
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# print("###")
# print(graph[0][1])
# print("###")
def bfs():
    global minNum
    queue = deque()
    queue.append((0,0)) #시작 위치는 1,1로 고정

    time = 0

    while queue:
        time += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == '1'):
                    graph[nx][ny] = int(graph[x][y]) + 1
                    queue.append((nx, ny))

    return time

ans = bfs()
print(graph[n-1][m-1])

# print(graph[n-1][m-1])

