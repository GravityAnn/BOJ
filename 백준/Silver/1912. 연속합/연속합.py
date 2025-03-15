import sys
input = sys.stdin.readline

#연속합
#임의의 수열
#연속된 몇 개의 수를 선택해서 가장 큰 합 만들기
#한 개 이상 택
#10, -4, 3, 1, 5, 6, -35, 12, 21, -1
#에서는 12, 21까지만 택

n = int(input())
dp = [0]*(n)
NumList = list(map(int, input().split()))

#10
#10, -4
#10, -4, 3
#10, -4, 3, 1
dp[0] = NumList[0]
maxNum = dp[0]

for i in range(1, n):
    a = dp[i-1] + NumList[i]#전부 더한 것
    b = 0

    if dp[i-1] < 0: #이전 dp가 음수라면
        b = NumList[i]

    dp[i] = max(a, b)

    if maxNum < dp[i]:
        maxNum = dp[i]

# print(dp)
print(maxNum)

