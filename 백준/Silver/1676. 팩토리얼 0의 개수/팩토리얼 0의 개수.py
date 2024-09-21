import sys
input =  sys.stdin.readline

n = int(input())

#n!에서 뒤에 처음 0이 아닌 숫자가 나올때까지 0의 개수를 구하는 프로그램
#10!에서 뒤에서쿠터 0이 아닌 숫자가 나올때까지의 0의 개수
cnt = 0

num = 1
for i in range(1, n+1):
    num *= i
num = list(str(num))
num = num[::-1]
for i in range(len(num)):
    if (num[i] == '0'):
        cnt += 1
        # print("더해줌", i)
    elif (num[i] != '0'):
        print(cnt)
        # print("이제 답", i)
        break
# s
