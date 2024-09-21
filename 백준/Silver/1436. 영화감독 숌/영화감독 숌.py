import sys
input = sys.stdin.readline

###6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
#666, 1666, 2666, 3666, ...
#n번째 영화의 제목은 n번째로 작은 저주의 숫자

n = int(input())

#666
#1666
#2666
#3666
#4666
#5666
#6660
#...
#6666
#...
#6669
#10666

cnt = 0
num = 666
# print(list(num))
while True:


    list1 = list(str(num))


    for i in range(2, len(list1)):
        if (list1[i] == '6'):
            if (list1[i-1] == '6'):
                if (list1[i-2] == '6'):
                    cnt += 1
                    break

    # print(num, cnt == n, cnt, n)
    if cnt >= n:
        print(num)
        # print(cnt)
        break

    num += 1