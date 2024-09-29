import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
#여학생 : n, 남학생 : m, 인턴쉽에 참여해야 하는 인원 : k
#여학생 2명과 남학생 1명이 팀을 결성하는 것이 원칙

while k:
    if n > 2*m:#여자가 너무 많은 경우
        n -= 1

    else: #남자가 너무 많거나, 같은 경우
        m -= 1
    k -= 1
team = min(n//2, m)
print(team)



