import sys
input = sys.stdin.readline
# from collections import deque

a = int(input())#배열 크기
lista = list(map(int, input().split()))#배열 내용
dp = [0]*a

#가장 긴 증가하는 부분 수열을 구하는 프로그램

for i in range(a):
    for j in range(i+1):
        if(lista[i]> lista[j]):
            lista[i]
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp)+1)

