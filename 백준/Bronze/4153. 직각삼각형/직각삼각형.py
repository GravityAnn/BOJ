import sys
from collections import deque
input = sys.stdin.readline

def func1(a, b, c):
    var1 = max(a, b, c)
    var2 = min(a, b, c)
    var3 = a+b+c -(var1+var2)
    if(var1*var1 == (var2*var2 + var3*var3)):
        print("right")
    else:
        print("wrong")


# n, m = map(int, input().split()) #세로, 가로
while(1):
    a, b, c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break

    func1(a, b, c)






