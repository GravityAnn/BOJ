import sys
input = sys.stdin.readline

k, n = map(int, input().split())
klist= []
for _ in range(k):
    klist.append(int(input()))

start = 1
end = max(klist)

while start <= end:
    mid = (start + end)//2
    LAN = 0 #랜 개수
    for line in klist:
        LAN += line//mid #랜의 개수 합

    if LAN >= n: #랜 개수가 너무 많다
        start = mid + 1 #길이 증가
    else:# 랜 개수가 일단 적다.
        end = mid - 1#길이 하락
    # print("start : ", start,"  mid : ", mid, "  end : ", end, "LAN : ", LAN)
print(end)
# print(LAN)