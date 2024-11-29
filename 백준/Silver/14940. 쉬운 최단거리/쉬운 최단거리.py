import sys
input = sys.stdin.readline
from collections import deque


n, m  = map(int, input().split())#세로 가로

graph = []
visited = [[0]*m for _ in range(n)]
queue = deque()
for _ in range(n):
    listg = list(map(int, input().split()))
    graph.append(listg)

#모든 지점에 대해서 목표지점까지의 거리를 구하여라

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(i, j):
    queue.append((i, j))

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < n and 0<= ny < m):
                if(graph[nx][ny] == 1 and visited[nx][ny] == 0):
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        if( graph[i][j] == 2):
            BFS(i, j)

for i in range(n):
    for j in range(m):
        if(visited[i][j] == 0 and graph[i][j] == 1):
            print(-1, end = " ")
        else:
            print(visited[i][j], end=" ")
    print("")













