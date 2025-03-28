import sys
input = sys.stdin.readline

#1, 2, 3 더하기 3
#n을 1, 2, 3의 합으로 나타내는 방법의 수
#1 : 1 -> 1
#2 : 11, 2 -> 2
#3 : 111, 12, 3, 21 -> 4
#4 : 1111, 112, 13, 121, 211, 22, 31 -> 4+2+1 = 7
#5 : 7 + 4 + 2 = 13
#6 : 13 + 7 + 4 = 24
#7 : 24 + 13 + 7 =44


dp = [0]*1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44
t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(8, n+1):
        if dp[i] == 0:
            dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%(1000000009)
    print(dp[n])
