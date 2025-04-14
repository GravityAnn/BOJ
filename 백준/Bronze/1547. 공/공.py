import sys
input = sys.stdin.readline

#공
#컵 3개를 일렬로
#1번에 공
#컵 위치를 바꿈(2, 1, 3)
#공의 위치는 바꾸지 않음

#컵 위치를 m번 바꿀 것이다.
m = int(input()) #섞은 횟수
list1 = []
for _ in range(m):
    list1.append(list(map(int, input().split())))
place = [1, 2, 3]

for i in range(m):
    a = place.index(list1[i][0])
    b = place.index(list1[i][1])

    temp = place[a]
    place[a] = place[b]
    place[b] = temp

    # print(place)
print(place[0])