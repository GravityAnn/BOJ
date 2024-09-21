# import sys
# input = sys.stdin.readline

n = int(input())
list2 = []
for _ in range(n):
    list1 = input()
    list2.append(list1)

list2 = set(list2)
list2 = list(list2)
list2.sort(key=len)
# print(list2)

l = 0
check = []

# print("123123    ",len(check))
for i in range(len(list2)):
    len1 = len(list2[i])
    # print("들어간것 ",i,"----",list2[i])

    if len(check) == 0: #체크가 비어있으면 다음것과 확인하자
        check.append(list2[i])
        # print("###",len(check[0]))
        len2 = len(check[0])
    else: #체크에 뭔가가 들어있으면
        if len2 != len1: #체크에 들어있는 것과 길이가 다르다?
            # print("길이???", len1, len2)
            check.sort()
            # print("정렬해봐", check)
            for ans in check:
                print(ans)
            check.clear()#출력후 비운다.
            check.append(list2[i]) #그리고 다시 넣는다.
            len2 = len(check[0])
        else: #체크에 있는 것과 길이가 같다?
            check.append(list2[i])
            len2 = len(check[0])
check.sort()
            # print("정렬해봐", check)
for ans in check:
    print(ans)





