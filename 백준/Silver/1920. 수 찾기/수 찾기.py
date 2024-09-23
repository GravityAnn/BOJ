import sys
input = sys.stdin.readline

#n개의 정수가 주어질때 x라는 정수가 있는지 확인
def bs(key):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if (list1[mid] == key):
            return 1
        elif (list1[mid] <= key):
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
list1 = list(map(int, input().split(" ")))
list1.sort()

m = int(input())
find = list(map(int, input().split(" ")))

for i in find:
    print(bs(i))






