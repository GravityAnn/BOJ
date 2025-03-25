import sys
input = sys.stdin.readline

#가장 긴 증가하는 부분 수열 4
n = int(input())
data = list(map(int, input().split()))
dp1 = [1] * n  # 각 위치에서의 LIS 길이는 최소 1
dp2 = [-1] * n # 경로 추적용 초기화


dp1[0] = 1
dp2[0] = -1
# print(data)
for i in range(1, n):#바로나
    for j in range(0, i):#나보다 작아야 하는 친구
        if data[i] > data[j]:
            if dp1[i] < dp1[j]+1:
                dp1[i] = dp1[j]+1
                dp2[i] = j


print(max(dp1))#답
list1 = []

length = dp1.index(max(dp1))
while length != -1:
    list1.append(data[length])
    length = dp2[length]
    # print("위치 : ",length)
list1.reverse()
print(*list1)
# print(dp2)
