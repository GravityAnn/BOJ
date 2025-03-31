import sys
input = sys.stdin.readline

#유래카 이론
#점들의 모음으로 표시 가능
#t = n(n+1)/2


def func1(n):
    return n*(n+1)/2

t = int(input())#테스트 수
for _ in range(t):
    mode = 0
    k = int(input())
    for i in range(1, 46):
        if mode == 1:
            break
        if k < func1(i):
            continue
        for j in range(1, 46):
            if mode == 1:
                break
            if k < func1(i) + func1(j):
                continue
            for l in range(1, 46):
                if mode == 1:
                    break
                if k < func1(i) + func1(j) + func1(l):
                    continue
                # print(func1(i), func1(j) , func1(l))
                if func1(i) + func1(j) + func1(l) == k:
                    mode = 1
                    break
    print(mode)

