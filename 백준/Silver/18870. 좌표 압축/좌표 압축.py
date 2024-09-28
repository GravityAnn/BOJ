import sys
input = sys.stdin.readline

n = int(input()) #n이 주어진다
ans = [0]*n

arr1 = list(map(int, input().split())) # 1~n
arr2 = sorted(list(set(arr1)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr1:
    print(dic[i], end=" ")
