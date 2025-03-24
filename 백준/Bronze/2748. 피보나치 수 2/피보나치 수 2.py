import sys
input = sys.stdin.readline

#피보나치 수2
#0과 1로 시작을 하고, 0, 1, 1, 2, 3, 5...
#n번째 피보나치 수를 구하는 프로그램을 작성하시오
n = int(input())
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])