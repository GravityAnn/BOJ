import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())#사람 수, 파티 수
kl = list(map(int, input().split()))# 진실을 아는 사람 리스트

#각 파티에 오는 사람수, 그들의 번호
vl = [list(map(int, input().split())) for _ in range(m)]
check = [False for _ in range(m)]

#거짓말을 할 수 있는 최댓값
cnt = 0
if(kl[0] == 0):#아무도 진실을 모른다면,
    cnt = 0#모든 파티에서 거짓말을 해도 된다.
else: #하지만 누군가가 진실을 안하면,
    #일단 그 사람이 있는 파티에선 진실을 말해야하고,
    #이것이 재귀로 돌아가겠지?
    list2 = set()
    for i in range(kl[0]):
        list2.add(kl[i+1])# 진실을 아는자 추가

    while list2:
        num = list2.pop()
        for i in range(m):
            if(num in vl[i][1:]) and (check[i] == False):
                check[i] = True
                for j in range(vl[i][0]):
                    list2.add(vl[i][j+1])

print(check.count(False))
