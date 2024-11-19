import sys
from collections import deque
input = sys.stdin.readline



def fun1(n, m):
    var1 = 0
    max = 0
    for i in range(1, min(n, m)+1):
        if((n%i==0) and (m%i==0)):
            if(max<i):
                max =i
    return max#최대 공약수

def fun2(n, m):
    min = n*m
    for i in range(1, m+1):
        var1 = n*i

        if(var1%m == 0):
            if(min > var1):
                min = var1
    return min

n, m = map(int, input().split()) #세로, 가로
print(fun1(n, m))
print(fun2(n, m))






