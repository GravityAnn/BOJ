from collections import deque

t = int(input()) #테스트 케이스
for _ in range(t):
    n = int(input())#편의점 개수
    queue = deque()
    x, y = map(int, input().split())#집
    now = [x, y, True]
    queue.append(now)
    
    shop = []
    for _ in range(n):
        r, c = map(int, input().split())#편의점
        shop.append([r, c, False])

    z, w = map(int, input().split())#목표 지점
    goal = [z, w, False]

    action = True

    def check(now, goal):
        global action
        if (abs(goal[0] - now[0]) + abs(goal[1] - now[1])) <= 1000:

            return True
        else:
            return False



    while queue and (action == True):
        # print("------------------")
        x, y, z = queue.pop()
        now = [x, y, z]

        if check(now, goal)== True: #현 위치와 목표지점 비교
            print("happy")
            # print(now)
            action = False
            break

        for place in shop:
            if (place[2] == False) and check(now, place) == True:
                # print("이동",now,"->", place)
                place[2] = True
                queue.append(place)

    if action == True:
        print("sad")


            

