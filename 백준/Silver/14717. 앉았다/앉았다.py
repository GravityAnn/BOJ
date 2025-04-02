import sys
input = sys.stdin.readline
from itertools import combinations
#앉았다.
#1~10 2장씩
#2장을 무작위로, 중복 불가X, 상대방 카드는 알수 x
#더 강한 족보가 승, 비길 수 있음
#1. 패어
#2. 더했을때 일의 자리 하이

a, b = map(int, input().split())
card = list(range(1, 11))*2
n = 0
# print(card)
card.remove(a)
card.remove(b)
# print(card)
list1 = list(combinations(card, 2))


total = len(list1)
n=0
if a == b:
    for pick in list1:
        if pick[0]==pick[1] and pick[0]>a:
            n+=1
            # print(pick[0], pick[1])
    p = 1-float(n)/total
    print(f"{p:.3f}")

else:
    x = (a+b)%10
    for pick in list1:
        if pick[0] != pick[1] and (pick[0] + pick[1])%10 < x:
            n+=1
    p = float(n) / total
    print(f"{p:.3f}")
