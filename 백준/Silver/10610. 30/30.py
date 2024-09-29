import sys
input = sys.stdin.readline

n = list(input().strip())
# print(n)

#30의 배수가 만들어지는지 확인
sum = 0
for i in n:
    sum += int(i)
if (sum % 3 != 0) or ('0' not in n):
    print(-1)
else:
    n.sort()
    n.reverse()
    print(''.join(n))


