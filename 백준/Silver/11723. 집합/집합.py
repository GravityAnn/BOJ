import sys
input = sys.stdin.readline



m = int(input())#연산수
queue = set()
for _ in range(m):
    a = list(map(str, input().split()))
    x = a[0]
    if (len(a) == 2):
        y = int(a[1])
    if(x == 'check'):
        if(y in queue):
            print(1)
        else:
            print(0)
    elif(x == 'add'):
        queue.add(y)
    elif (x == 'remove'):
        queue.discard(y)
    elif (x == 'toggle'):
        if (y in queue):
            queue.discard(y)
        else:
            queue.add(y)
    elif (x == 'all'):
        queue = set([i for i in range(1, 21)])
    elif (x == 'empty'):
        queue = set()





