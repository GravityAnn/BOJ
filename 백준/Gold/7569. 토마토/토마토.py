import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = []
queue = deque()

# 모든 상자를 읽으며 익은 토마토(=1) 위치 큐에 저장
for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, input().split()))
        for k, v in enumerate(row):
            if v == 1:
                queue.append((i, j, k))
        layer.append(row)
    box.append(layer)

days = -1
while queue:
    for _ in range(len(queue)):
        x, y, z = queue.popleft()
        for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = 1
                queue.append((nx, ny, nz))
    days += 1

# 익지 않은 토마토가 있으면 -1
for i in range(h):
    for j in range(n):
        if 0 in box[i][j]:
            print(-1)
            sys.exit()

print(days)