import sys
input = sys.stdin.readline
# from collections import deque
import heapq
def func2(heap, x):
    heapq.heappush(heap, x)

def func1(heap):
    print(heapq.heappop(heap))


n = int(input())
cnt = 0
heap = []
for _ in range(n):
    x = int(input())
    if(x == 0):
        if(cnt == 0):
            print(0)
        else:
            func1(heap)
            cnt -= 1
    else:
        func2(heap, x)
        cnt += 1