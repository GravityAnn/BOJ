import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]
visit = [[0] * c for _ in range(r)]  # 방문 배열 수정

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    fire = deque()

    # 초기 지훈이 위치 및 불 위치 저장
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'J':  # 지훈이 위치
                queue.append((i, j, 0))  # (x, y, 시간)
                visit[i][j] = 1
            elif maze[i][j] == 'F':  # 불 위치
                fire.append((i, j))

    while queue:
        # 1. 불이 먼저 확산
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.':
                    maze[nx][ny] = 'F'
                    fire.append((nx, ny))

        # 2. 지훈이 이동
        for _ in range(len(queue)):
            x, y, time = queue.popleft()

            # 탈출 성공
            if x == 0 or x == r - 1 or y == 0 or y == c - 1:
                return time + 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.' and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append((nx, ny, time + 1))

    return "IMPOSSIBLE"

print(BFS())
