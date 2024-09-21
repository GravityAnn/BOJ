# import sys
# input = sys.stdin.readline

# mxn개 크기의 보드를 잘라서 8x8크기의 체스판을 만들려고 한다.
#변을 공유하는 두 사각형은 다른 색으로 칠해져야 하며 체스판을 색칠하는 경우는
#두 가지 뿐이다.
#지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str,input())))

def check1(sn, sm):
    cnt1 = 0
    cnt2 = 0
    if graph[sn][sm] == 'W':
        # print("W 탐색해봅니다. ", sn, sm)
        for i in range(8):
            for ii in range(8):
                if (i+ii) % 2 == 0:
                    if graph[sn + i][sm + ii] == 'B':
                        cnt1 += 1
                    if graph[sn + i][sm + ii] == 'W':
                        cnt2 += 1
                        # print(sn + i, sm + ii)
                else:
                    if graph[sn + i][sm + ii] == 'W':
                        cnt1 += 1
                    if graph[sn + i][sm + ii] == 'B':
                        cnt2 += 1
    else:
        # print("B 탐색해봅니다. ", sn, sm)
        for i in range(8):
            for ii in range(8):
                if (i+ii) % 2 == 0:
                    if graph[sn + i][sm + ii] == 'W':
                        cnt1 += 1
                    if graph[sn + i][sm + ii] == 'B':
                        cnt2 += 1
                else:
                    if graph[sn + i][sm + ii] == 'B':
                        cnt1 += 1
                    if graph[sn + i][sm + ii] == 'W':
                        cnt2 += 1
    return cnt1, cnt2



min = 64
for i in range(n):
    for ii in range(m):
        if 0 <= i <= n-8:
            if 0 <= ii <= m - 8: #8칸씩 자르는 것이 가능한 상태에서
                sn = i
                sm = ii
                find1, find2 = check1(sn, sm)
                # print(find1)
                if min >= find1:
                    min = find1
                if min >= find2:
                    min = find2


print(min)

