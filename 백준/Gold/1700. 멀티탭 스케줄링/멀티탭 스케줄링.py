import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())# 구멍 개수, 총 사용횟수
list1 = list(map(int, input().split()))# 순서와 이름
plug = []
cnt =0

for i in range(k):
    use = False

    # 플러그가 비어있으면 채우기
    if (len(plug) < n) and (not list1[i] in plug):
        plug.append(list1[i])

    #사용
    if list1[i] in plug:
        use = True

    #사용못함
    while (not use):

        max_time = -1
        pick = -1
        for p in plug:
            if not p in list1[i+1:]:
                pick = p
                # print("첫번째 케이스", end=" ")
                break

            else:
                this_time = list1[i+1:].index(p)
                if(max_time < this_time):
                    # print("두번째 케이스", end=" ")
                    # print(max_time ,this_time)
                    max_time = this_time
                    pick = p
        # print("pick", pick)
        plug.remove(pick)
        cnt += 1

        if (len(plug) < n) and (not list1[i] in plug):
            plug.append(list1[i])

        # 사용
        if list1[i] in plug:
            use = True

    # print(plug)
print(cnt)
