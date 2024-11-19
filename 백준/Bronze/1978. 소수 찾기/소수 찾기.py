import sys
input = sys.stdin.readline

# n, m = map(int, input().split()) #세로, 가로
#가장 왼쪽 아래 칸에 위치해있다.
#방문한 칸이 5개 이상이라면 이동 방법을 모두 한 번씩 사용해야 한다.
def find(list1):
    count = 0
    for num in list1:
        check = 0
        if(num >= 2):
            for i in range(2, num):
                if(num%i == 0):
                    check=1
                    break
            if(check == 0):
                count += 1
    return count




n = int(input())
list1 = list(map(int, input().split()))
list1.sort()

print(find(list1))









