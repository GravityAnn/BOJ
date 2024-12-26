import sys
input = sys.stdin.readline

n = list(input())
n = n[0:len(n)-1]
listn = []

for i in range(len(n)):
    number = int(n[i])
    # print("number : ", number)
    for j in range(2, -1, -1):
        if(number >= 2**j):
            # print(number, " > ", 2**j)
            listn.append(1)
            number -= 2**j
            # print(listn)
        else:
            # print(number, " < ", 2 ** j)
            listn.append(0)
            # print(listn)
# print(listn)
for i in range(len(listn)):
    if(len(listn) == 3):
        if(listn[0] == 0 and listn[1] == 0 and listn[2] ==0):
            print(0)
            break

    if(listn[i] == 1):
        for j in range(i, len(listn)):
            print(listn[j], end="")
        break
