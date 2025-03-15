import sys
input = sys.stdin.readline

#이친수
#이진수는 0으로 시작하지 않는다.
#이친수는 1이 두번 연속 나오지 않는다.

n = int(input())
dp = [0]*(n+2)

dp[1] = 1 #1
dp[2] = 1 #1(0)

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
# print(dp)
print(dp[n])

