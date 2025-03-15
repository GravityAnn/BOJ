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
    if NumList[i] > NumList[i-1]:
        x = 0
        for j in range(0, i):
            if (NumList[i] > NumList[j]):
                if (x <= dp[j]):
                    x = dp[j]

        dp[i] = NumList[i] + x
        # print(NumList[i] ,x)

    if NumList[i] <= NumList[i-1]:
        x = 0
        for j in range(0, i):
            if (NumList[i] > NumList[j]):
                if (x <= dp[j]):
                    x = dp[j]
                    # print(x)
        dp[i] = NumList[i] + x
        # print(NumList[i],x)

    if maxNum < dp[i]:
        maxNum = dp[i]

# print(dp)
print(maxNum)

