import sys
from collections import deque

n, m = map(int, input().split())#표의 크기, 합을 구해야 하는 횟수
graph = [list(map(int, input().split())) for _ in range(n)]
question = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(n)]
# print(n, m)
# print(graph)
# print(question)
# print(dp)


def make(graph, dp):
    x = 0
    y = 0
    dp[x][y] = graph[x][y]
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0:
                    dp[i][j] = graph[i][j]
                else:
                    dp[i][j] = graph[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = graph[i][j] + dp[i-1][j]

            else:
                dp[i][j] = graph[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
make(graph, dp)
# print(dp)
def func1(x, y, z, w):
    global dp
    if x == 0:
        if y == 0:
            return dp[z][w]
        else:
            return dp[z][w] - (dp[z][y-1])

    elif y == 0:
        return dp[z][w] - dp[x-1][w]

    else:
        return dp[z][w] - (dp[z][y-1] + dp[x-1][w]) + dp[x-1][y-1]

for i in range(len(question)):
    print(func1(question[i][0]-1, question[i][1]-1, question[i][2]-1, question[i][3]-1))



            

