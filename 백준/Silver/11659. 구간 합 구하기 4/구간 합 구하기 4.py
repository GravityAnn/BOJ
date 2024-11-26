import sys
input = sys.stdin.readline

#n개의 수가 주어졌을 때 i~j까지의 합을 구하는 프로그램

def sumPre(list1):
    list2 = [0]
    list2[0] = list1[0]
    for i in range(1,len(list1)):
        list2.append(list1[i]+list2[i-1])
    return list2
def func1(list2, x, y):
    if(x == 1):
        ans = list2[y-1]
    else:
        ans = list2[y-1] - list2[x-2]
    print(ans)

n, m = map(int, input().split())
list1 = list(map(int, input().split())) #n개의 숫자들
list2 = sumPre(list1)
for _ in range(m):
    x, y = map(int, input().split())
    func1(list2, x, y)

