# import sys
# input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# print(n, m)
list1 = [list(input()) for _ in range(n)]
max_count = 0
#이동시간 1시간
#육지로만 이동 가능
#보물은 최단거리로 이동했을때 가장 긴 시간이 걸리는 육지 두곳에 위치
#반드시 최단거리로 움직일것

#이때 가낭 오래 걸리는 시간을 구하시오
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(i, j):
    global max_count
    queue.append([i, j])
    visit[i][j] = 1

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if(0 <= nx < n and 0 <= ny < m) and (list1[nx][ny] == 'L') and (visit[nx][ny] == 0):
                visit[nx][ny] = visit[x][y] + 1
                if(visit[nx][ny] >= max_count):
                    max_count = visit[nx][ny]
                queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if(list1[i][j] == 'L'):
            visit = [[0]*m for _ in range(n)]
            queue = deque()
            BFS(i, j)
            queue.clear()
            # print("출발 : [",i,",",j,"]")
            # for k in range(n):
            #     print(visit[k])
            # print("----------------------")
print(max_count-1)
