import sys
input = sys.stdin.readline

#부분 수열
#순서가 있는 부분 수열
#첫 번째 수가 큰 쪽이 사전 순으로 나중 수열
#수열의 길이가 n인 수열A, 길이가 m인 수열B
#두 수열이 공통으로 같는 수열중 사전 순으로 가장 나중인 것을 구하시오

n = int(input())
lista = list(map(int, input().split()))
m = int(input())
listb = list(map(int, input().split()))
dp = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

# 뒤에서 앞으로!
for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            # 1) A[i]를 스킵하거나, B[j]를 스킵하는 경우(둘 중 사전 순으로 더 나은 쪽)
            skip_case = max(dp[i + 1][j], dp[i][j + 1])

            # 2) A[i] == B[j]라면, 그 원소를 채택하는 경우
            if lista[i] == listb[j]:
                take_case = [lista[i]] + dp[i + 1][j + 1]
                # 스킵 vs 채택 중 사전 순 비교
                dp[i][j] = max(skip_case, take_case)
            else:
                dp[i][j] = skip_case


result = dp[0][0]
print(len(result))
print(*result)
