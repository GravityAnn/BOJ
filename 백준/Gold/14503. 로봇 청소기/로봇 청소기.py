import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 방향: 0북, 1동, 2남, 3서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d):
    return (d + 3) % 4

count = 0

while True:
    if not visited[r][c]:
        visited[r][c] = True
        count += 1

    
    moved = False
    for _ in range(4):
        d = turn_left(d)
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and not visited[nr][nc]:
            r, c = nr, nc
            moved = True
            break

    if not moved:
        br, bc = r - dx[d], c - dy[d]
        if 0 <= br < N and 0 <= bc < M and room[br][bc] == 0:
            r, c = br, bc  # 후진
        else:
            break 

print(count)
