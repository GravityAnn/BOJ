#1012
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) #가로, 세로, 배추가 있는 위치 개수
    graph = [[0]* n  for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1



    def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        else:
            if (graph[x][y] == 1):
                graph[x][y] = 0
                for i in range(4):
                    dfs(x + 1, y)
                    dfs(x, y + 1)
                    dfs(x - 1, y)
                    dfs(x, y - 1)
                    return True
            return False

    cnt = 0
    for a in range(m):
        for b in range(n):
            if (dfs(a, b) == True):
                cnt += 1
    print(cnt)


