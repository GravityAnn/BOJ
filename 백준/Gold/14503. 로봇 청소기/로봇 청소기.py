import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
cnt = 0
action = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def func1(x, y, d):
    global cnt
    action = True
    while action:
        # print(x, y, cnt)
        #1번 행동
        if (visit[x][y] == False) and (graph[x][y] == 0):
            #방문한적 없고, 방이면
            visit[x][y] = True#청소
            cnt += 1

        #3번 행동
        turn = False
        for _ in range(4):
            d = (d+3)%4
            nx = x + dx[d]
            ny = y + dy[d] #일단 방향 전환하고
            if(0 <= nx < n) and (0 <= ny < m):
                if(visit[nx][ny] == False) and (graph[nx][ny] == 0):
                    x = nx
                    y = ny
                    turn = True
                    break#방향 전환

        #2번 행동
        if turn == False:#전부다 막혀있거나 이동을 안했으면,
            nx = x - dx[d]
            ny = y - dy[d] #후진
            if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 0):
                    x = nx
                    y = ny
            else:
                action = False
                break






func1(x, y, d)
print(cnt)