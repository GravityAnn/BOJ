import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) #테스트 케이스
for _ in range(t):
    l = int(input()) # l x l 크기의 체스판


    graph = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    now = list(map(int, input().split()))
    des = list(map(int, input().split()))

    queue = deque()

    def bfs():
        queue.append(now)
        visited[now[0]][now[1]]
        while queue:
            x, y = queue.popleft()

            if x == des[0] and y == des[1]:
                return 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < l and 0 <= ny < l:
                    if nx == des[0] and ny == des[1]:
                        visited[nx][ny] = True
                        return graph[x][y] + 1

                    if visited[nx][ny] == False:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[x][y] + 1
    ans = bfs()
    print(ans)


