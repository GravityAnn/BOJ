import sys

input = sys.stdin.readline

t = int(input())  # 테스트 개수
for _ in range(t):
    n = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    # DP 테이블 초기화
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = list1[0]
    dp[1][0] = list2[0]

    if n > 1:
        dp[0][1] = list2[0] + list1[1]
        dp[1][1] = list1[0] + list2[1]

    # DP 계산
    for i in range(2, n):
        dp[0][i] = list1[i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = list2[i] + max(dp[0][i - 1], dp[0][i - 2])

    # 결과 출력
    print(max(dp[0][n - 1], dp[1][n - 1]))
