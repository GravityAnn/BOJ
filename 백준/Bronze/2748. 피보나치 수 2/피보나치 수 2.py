#숨바꼭질
import sys
input = sys.stdin.readline


n = int(input())
dp = [0]*(n+5)

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(3,n+1):
    dp[i+1] = dp[i]+dp[i-1]


print(dp[n+1])

