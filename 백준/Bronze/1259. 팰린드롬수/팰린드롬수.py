
#랠린드롬수

while (True):
    n = list(input())
    # print(n)

    if n == ['0']:
        break

    if n == n[::-1]:  # 문자열을 뒤집어서 비교합니다.
        print("yes")
    else:
        print("no")


