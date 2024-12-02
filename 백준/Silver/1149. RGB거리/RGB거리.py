import sys
input = sys.stdin.readline

#1번집은 2번집과 색이 다를 것
#모든 집은 이전 집과 색이 다를 것
#각 집은 양 옆과 색이 달라야 한다.

n = int(input())#집 개수
dp = [[0, 0, 0] for _ in range(n)]
# print(dp)
color = list(map(int, input().split()))
dp[0] = color

for i in range(1, n):
    color = list(map(int, input().split()))
    for x in range(3):
        if(x==0):
            dp[i][0] = color[0] + min(dp[i-1][1], dp[i-1][2])
        elif(x==1):
            dp[i][1] = color[1] + min(dp[i-1][0], dp[i-1][2])
        if (x == 2):
            dp[i][2] = color[2] + min(dp[i-1][1], dp[i-1][0])
print(min(dp[n-1]))


