import sys
input = sys.stdin.readline

#6단계 법칙 이씨와 민씨는 몇단계일까
#이씨-천씨-최씨-김씨-김씨-민씨
#백준 유저중에서 가장 케빈 베이컨 수가 작은 사람을 찾아보자


INF = int(1e9)
n, m = map(int, input().split())#유저수, 관계쑤
mem = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    mem[a][b] = 1
    mem[b][a] = 1

for i in range(n+1):
    mem[i][i] = 0
    mem[i][0] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            mem[i][j] = min(mem[i][j], mem[i][k] + mem[k][j])

ans = 0
min_num = INF
for i in range(1, n+1):
    # print(mem[i])
    num = sum(mem[i])
    if min_num > num:
        min_num = num
        ans = i
print(ans)



