#불
from collections import deque

t = int(input())#테스트 케이스
for _ in range(t):
    w, h = map(int, input().split())#너비, 높이
    visit = [[0]*w for _ in range(h)]
    graph = [list(input()) for _ in range(h)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def BFS():
        fireQueue = deque()
        mainQueue = deque()
    
        #상근이와 불의 위치 확인
        for i in range(h):
            for j in range(w):
                if(graph[i][j] == '*'):
                    fireQueue.append((i, j))
                elif(graph[i][j] == '@'):
                    mainQueue.append((i, j, 0))
                    visit[i][j] = 1#지훈이 위치
        
    
        while (mainQueue):
            # for i in range(h):
            #     print(graph[i])
            # print("")
    
            # 불의 이동
            for _ in range(len(fireQueue)):
                fx, fy = fireQueue.popleft()
    
                for i in range(4):
                    nfx = fx + dx[i]
                    nfy = fy + dy[i]
                    # 방 내부이면서, 빈칸 혹은 상근이 위치이면
                    if(0<=nfx<h) and (0<=nfy<w) and ((graph[nfx][nfy]=='.') or (graph[nfx][nfy]=='@')):
                        graph[nfx][nfy] = '*'
                        # print("불 이동", graph[nfx][nfy])
                        fireQueue.append([nfx, nfy])#불 이동
    
            #상근이 이동
            for _ in range(len(mainQueue)):
                x, y, time = mainQueue.popleft()
    
                if (x==0 or x==h-1) or (y==0 or y==w-1):
                    return time + 1
    
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
    
                    if(0<=nx<h) and (0<=ny<w) and (graph[nx][ny] == '.') and visit[nx][ny] == 0:
                        mainQueue.append((nx, ny, time+1))
                        # print(nx, ny,"들어감")
                        graph[nx][ny] = '@'
                        visit[nx][ny] = 1
        return "IMPOSSIBLE"
    
    print(BFS())

