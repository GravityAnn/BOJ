import sys
input = sys.stdin.readline

#2승의 곱으로 이루어진 정사각형 종이. 
#하얀색 종이와 파란색 종이의 합


def func1(list1):
    # print("들어간 리스트 : ", list1, "길이 : ",len(list1),"[1 : ", sum(sum(list1, [])),"]")
    global white, color
    if (sum(sum(list1, [])) == len(list1)*len(list1)):
        color += 1
        return
    elif (sum(sum(list1, [])) == 0):
        white += 1
        return
    if (len(list1) != 1):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for j in range(len(list1)//2):
            l1.append(list1[j][:len(list1)//2])#2사분면
            l2.append(list1[j][len(list1)//2:])#1사분면
            l3.append(list1[j+len(list1) // 2][:len(list1) // 2])#3사분면
            l4.append(list1[j+len(list1) // 2][len(list1) // 2:])#4사분면
        func1(l1)
        func1(l2)
        func1(l3)
        func1(l4)


n = int(input())
white = 0
color = 0
list1 = []
for _ in range(n):
    line = list(map(int, input().split()))
    list1.append(line)

func1(list1)
print(white)
print(color)