from collections import deque
#벽 부수고 이동하기
#0이동가능, 1벽
#이동하는 도중 한개의 벽을 부수고 이동하는 것이 더
#좋아면 한 개까지 부수고 이동하여도 된다.
#이동은 상하좌우

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 3차원 방문 배열

queue = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    #시작위치
    queue.append((0, 0, 0, 1))
    visit[0][0][1] = 1

    while queue:
        x, y, count, power = queue.popleft()


        #만약 도착했다면,
        if (x==n-1) and (y==m-1):
            return count+1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if power == 1:
                if (0 <= nx < n) and (0 <= ny < m) and (visit[nx][ny][0] == 0) and (graph[nx][ny] == '1'):
                    queue.append((nx, ny, count + 1, 0))
                    visit[nx][ny][0] = 1

            if (0 <= nx < n) and (0 <= ny < m) and (visit[nx][ny][power] == 0) and (graph[nx][ny] == '0'):
                queue.append((nx, ny, count + 1, power))
                visit[nx][ny][power] = 1
    return -1

print(BFS())
