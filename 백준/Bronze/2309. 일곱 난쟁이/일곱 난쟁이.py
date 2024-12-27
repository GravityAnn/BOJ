import sys
input = sys.stdin.readline

list1 = [int(input()) for _ in range(9)]

target = sum(list1) -100
min1 = 0
min2 = 0
target1 = 0
target2 = 0
tmp = 0
# print(list1)
for i in range(9):
    min1 = 0
    min2 = i
    for j in range(i+1, 9):
        if(list1[min2] > list1[j]):
            min2 = j#위치기억
        # print("i번 : ", i, " target1 : ", list1[i], "(", min2, ") target2 : ", list1[j], "(", j, ")")
    tmp = list1[i]
    list1[i] = list1[min2]
    list1[min2] = tmp
found = False
for i in range(9):
    for j in range(i+1, 9):
        if (list1[i] + list1[j] == target):
            target1 = list1[i]
            target2 = list1[j]
            found = True
            break
    if found:
        break
for i in range(9):
    if(list1[i] != target1) and (list1[i] != target2):
        print(list1[i])





