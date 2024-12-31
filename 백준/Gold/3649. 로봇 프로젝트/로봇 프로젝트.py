import sys
input = sys.stdin.readline

#구멍의 너미x, 두조각의 길이의 합은 구멍의 너비와 반드시 일치해야만
while True:
    try:
        x = int(input())*(10000000) #구멍의 너비 #cm 단위
        n = int(input()) #레고 개수
        l = [int(input()) for i in range(n)]#나노미터 단위
        # 10cm = 10,000,000nm
        l.sort()
        ans = []
        left = 0
        right = n-1
        while(left < right):
            x = x
            # print(l[left] + l[right])
            if(l[left] + l[right] < x):
                left += 1
            elif(l[left] + l[right] > x):
                right -= 1
            else:
                ans.append(left)
                ans.append(right)
                break
        if(ans):
            print("yes", l[ans[0]], l[ans[1]])
        else:
            print("danger")
    except:
        break


