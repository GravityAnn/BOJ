import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())#개수, 시작, 한계
dp = [-1]*(m+1)
dp2 = [-1]*(m+1)
dp[s] = 0
# print(dp)

#현재p, i곡 연주하기 전이라면, i곡은 p+v[i] or p-v[i]
#불가하면 -1
list1 = list(map(int, input().split()))

for i in range(n):
    move = False
    for j in range(m+1):
        if dp[j] == i:
            x = j + list1[i]
            y = j - list1[i]
            if 0 <= x <= m:
                dp2[x] = i+1
                move=True
            if 0 <= y <= m:
                dp2[y] = i+1
                move = True
    dp = dp2[:]
    if not move:
        break


dp.reverse()
if n in dp:
    print(m - dp.index(n))
else:
    print(-1)