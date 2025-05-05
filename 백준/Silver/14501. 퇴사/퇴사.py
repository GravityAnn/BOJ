import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
for i in range(n):
    a, b = map(int, input().split())
    if (i + a ) <= n+1:
        for j in range(i+a, n+1):
            dp[j] = max(dp[i] + b, dp[j])
    # print(dp)
print(max(dp))
