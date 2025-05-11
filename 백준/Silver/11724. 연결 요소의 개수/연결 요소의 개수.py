import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
visit = [False]*n
count = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

def BFS(s):
    queue = deque()
    queue.append(s)
    visit[s] = True

    while queue:
        x = queue.popleft()
        for i in range(n):
            if (graph[x][i] == 1 and visit[i] == False):
                queue.append(i)
                visit[i] = True

for s in range(n):
    if visit[s] == False:
        BFS(s)
        count += 1

print(count)