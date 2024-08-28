#10026
import sys
sys.setrecursionlimit(10**6 + 1)
# input = sys.stdin.readline

n = int(input()) #n개의 줄이 주어진다.
visited_r = [[False]*n for _ in range(n)]
visited_b = [[False]*n for _ in range(n)]
visited_g = [[False]*n for _ in range(n)]
visited_rg = [[False]*n for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(input()))


#RED
def dfs_r(x, y):
    if (0<= x < n) and (0<= y < n) and (visited_r[x][y] == False):
        visited_r[x][y] = True

        if graph[x][y] == 'R':
            dfs_r(x + 1, y)
            dfs_r(x - 1, y)
            dfs_r(x, y + 1)
            dfs_r(x, y - 1)
            return 0
        return 0
    return 0
def dfs_b(x, y):
    if (0<= x < n) and (0<= y < n) and (visited_b[x][y] == False):
        visited_b[x][y] = True

        if graph[x][y] == 'B':
            dfs_b(x + 1, y)
            dfs_b(x - 1, y)
            dfs_b(x, y + 1)
            dfs_b(x, y - 1)
            return 0
        return 0
    return 0
def dfs_g(x, y):
    if (0<= x < n) and (0<= y < n) and (visited_g[x][y] == False):
        visited_g[x][y] = True

        if graph[x][y] == 'G':
            dfs_g(x + 1, y)
            dfs_g(x - 1, y)
            dfs_g(x, y + 1)
            dfs_g(x, y - 1)
            return 0
        return 0
    return 0
def dfs_rg(x, y):
    if (0<= x < n) and (0<= y < n) and (visited_rg[x][y] == False):
        visited_rg[x][y] = True

        if (graph[x][y] == 'G') or (graph[x][y] == 'R'):
            dfs_rg(x + 1, y)
            dfs_rg(x - 1, y)
            dfs_rg(x, y + 1)
            dfs_rg(x, y - 1)
            return 0
        return 0
    return 0


cnt_1 = 0
cnt_2 = 0
cnt1 = []
cnt2 = []
for a in range(n):
    for b in range(n):
        if (visited_r[a][b] == False) and (graph[a][b] == 'R'):
            dfs_r(a, b)
            cnt_1 += 1


        if (visited_b[a][b] == False) and (graph[a][b] == 'B'):
            dfs_b(a, b)
            cnt_1 += 1
            cnt_2 += 1
        if (visited_g[a][b] == False) and (graph[a][b] == 'G'):
            dfs_g(a, b)
            cnt_1 += 1
        if (visited_rg[a][b] == False) and ((graph[a][b] == 'R') or (graph[a][b] == 'G')):
            dfs_rg(a, b)
            cnt_2 += 1
print(cnt_1, cnt_2)


