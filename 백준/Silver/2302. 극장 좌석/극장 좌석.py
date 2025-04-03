import sys
input = sys.stdin.readline

#극장 좌석
#1~n까지 번호, 한줄
#일반 고객 : 좌우로 이동 가능
#중요 고객 : 반드시 자기 좌석
#서로 다른 방법 구하기

n = int(input())#좌석개수
m = int(input())#고정석 개수
fixed = [0]+ [int(input()) for _ in range(m)] + [n+1]
# print(n, m)
# print(fixed)
dp = [0]*(n+9)
dp[0] = 1
dp[1] = 1 #1
dp[2] = 2 #1, 21
dp[3] = 3 #123 1+2
dp[4] = 5 #1234 1+3+1
dp[5] = 8 #12345 1+4+2+1
size1 = 0
for i in range(1, len(fixed)):
    size2 = fixed[i] - fixed[i - 1] - 1
    size1 = max(size1, size2)
# print(size1)

for j in range(5, size1+1):
    dp[j] = dp[j-1]+dp[j-2]

ans = 1
for i in range(1, len(fixed)):
    size = fixed[i]-fixed[i-1]-1
    ans *= dp[size]
    # print("계산중1",ans)
print(ans)