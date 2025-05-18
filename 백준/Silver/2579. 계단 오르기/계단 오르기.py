import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n)
list1 = [int(input()) for _ in range(n)]
# print(list1)

for i in range(n):
    if i == 0:
        dp[0] = list1[0]
    elif i == 1:
        dp[1] = list1[0] + list1[1]
    elif i ==2:
        dp[2] = max(list1[0]+list1[2], list1[1]+list1[2])
    else:
        a = list1[i] + dp[i-2]
        b = dp[i-3] + list1[i] + list1[i-1]
        dp[i] = max(a, b)
print(dp[-1])

