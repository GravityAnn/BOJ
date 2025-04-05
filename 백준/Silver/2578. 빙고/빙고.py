import sys
input = sys.stdin.readline

#빙고
#25개칸
#가장 먼저 외치는 사람이 승자
#몇번째 수를 부른 후에 철수가 빙고를 외치는지

list1 = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
list2 = [list(map(int, input().split())) for _ in range(5)]
# print(visit)
# print(list1)
# print(list2)

def check():
    total = 0
    for i in range(5):#가로
        count = 0
        for j in range(5):
            if visit[i][j] == 1:
                count += 1
        if count == 5:
            total += 1

    for j in range(5):#세로
        count = 0
        for i in range(5):
            if visit[i][j] == 1:
                count += 1
        if count == 5:
            total += 1

    count = 0
    for i in range(5):
        if visit[i][i] == 1:
            count += 1
    if count == 5:
        total += 1

    count = 0
    for i in range(5):
        if visit[i][4-i] == 1:
            count = count + 1
    if count == 5:
        total += 1
    return total

ans = 0
ans_count = 0
for i in range(5):
    for j in range(5):
        a = list2[i][j]
        ans += 1

        for x in range(5):
            for y in range(5):
                if list1[x][y] == a:
                    visit[x][y] = 1
        # print("ans : ",ans)
        # for q in range(5):
            # print(visit[q])
        # print("현재 빙고 개수",check())
        if check() >= 3:
            print(ans)
            exit()
        # print("\n")




