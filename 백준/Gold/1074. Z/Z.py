import sys
from collections import deque
input = sys.stdin.readline



def aboutN(n, r, c):
    if(n == 1):
        if(r==1):
            if(c == 1):
                return 3
            else:
                return 2
        else:
            if (c == 1):
                return 1
            else:
                return 0
    else:
        if(r >= 2**(n-1)):
            if(c >= 2**(n-1)):
                return 3*((2**(n-1))*(2**(n-1))) + aboutN(n-1, r-(2**(n-1)), c-(2**(n-1)))
            else:
                return 2*((2**(n-1))*(2**(n-1))) + aboutN(n-1, r-(2**(n-1)), c)
        else:
            if(c >= 2**(n-1)):
                # print((2**(n-1))*(2**(n-1)))
                return ((2**(n-1))*(2**(n-1))) + aboutN(n-1, r, c-(2**(n-1)))
            else:
                return aboutN(n-1, r, c)

n, r, c = map(int, input().split())
print(aboutN(n, r, c))

# arr = [[0 for j in range(5)] for i in range(5)]
# for i in range(1, 5):
#     for j in range(1, 5):
#         arr[i][j] = aboutN(5, i-1, j-1)
#
# print(arr)




