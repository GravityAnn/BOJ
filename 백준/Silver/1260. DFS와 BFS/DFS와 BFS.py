import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

def DFS():
    visit = [False for _ in range(n)]
    stack = [v-1]

    while stack:
        x = stack.pop()
        if not visit[x]:
            visit[x] = True
            print(x + 1, end=" ")
        for i in range(n-1,-1,-1):
            if (graph[x][i] == 1 and visit[i] == False):
                stack.append(i)

DFS()

print("")
def BFS():
    visit = [False for _ in range(n)]
    queue = deque()
    queue.append(v-1)
    visit[v - 1] = True

    while queue:
        x = queue.popleft()
        print(x+1, end=" ")
        for i in range(n):
            if (graph[x][i] == 1 and visit[i] == False):
                queue.append(i)
                visit[i] = True

BFS()