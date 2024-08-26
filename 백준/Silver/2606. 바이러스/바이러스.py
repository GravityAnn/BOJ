#2606
import sys
input = sys.stdin.readline

n = int(input()) #컴퓨터 개수
m = int(input()) #연결된 컴퓨터 쌍의 개수

graph = [[False]*(n+1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

cnt = 0
def dfs(v):
    global cnt
    if (visited[v] == False):
        visited[v] = True
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i]:
                dfs(i)

dfs(1)
print(visited.count(True)-1)
