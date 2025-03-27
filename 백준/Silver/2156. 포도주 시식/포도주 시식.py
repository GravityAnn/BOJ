import sys
input = sys.stdin.readline

#포도주 시식
#잔을 선택하면 다 마시고, 다시 원위치
#연속 3잔 마실 수 X

#최대한 많이 마시고 싶음.
n = int(input())#잔 개수
wine = [0]*10000
for i in range(n):
    wine[i] = int(input())
dp = [0]*10000

dp[0] = wine[0]
dp[1] = wine[0]+wine[1]
dp[2] = max(dp[1], wine[0]+wine[2], wine[1]+wine[2])


for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1])

print(max(dp))