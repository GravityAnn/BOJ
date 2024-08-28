import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())  # 가로, 세로

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    # 시작점들(익은 토마토가 있는 위치들)을 큐에 추가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    days = -1  # 모든 토마토가 익는 데 걸린 일수를 세기 위한 변수
    while queue:
        days += 1  # 하루가 지나감
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))

    # 만약 모든 토마토가 익지 않았다면, -1 반환
    for row in graph:
        if 0 in row:
            return -1

    return days


result = bfs()
print(result)
