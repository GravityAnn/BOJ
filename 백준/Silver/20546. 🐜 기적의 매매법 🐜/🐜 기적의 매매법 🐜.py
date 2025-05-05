import sys
input = sys.stdin.readline

##성민
#33매매법, 전량매매
# 3일 상승 -> 매도
# 유지는 괜찮
#3일 하락 -> 매수
# 유지는 괜찮
#14일간 대결
#자산 = 현금 + 1월14일 주가 * 가격

##준현
#BNP

money = int(input())
m1 = money#준현
m2 = money#성민
date = list(map(int, input().split()))#날짜
stock1 = 0
stock2 = 0

#준현
for price in date:
    stock1 += m1//price
    m1 = m1%price
# print(stock1)

#성민
up_count = 0
down_count = 0
p1 = date[0]
for price in date:
    if p1 < price:#상승
        up_count += 1
        # print("작동?", up_count,p1,price)
        if up_count >= 3:#3번
            m2 += stock2*price #매도
            # print("매도",stock2,m2,price)
            stock2 = 0
        down_count = 0

    if p1 > price:#하락
        down_count += 1
        if down_count >= 3:#3번
            stock2 += m2//price#매수
            m2 = m2%price
            # print("매수", stock2, m2,price)
        up_count = 0
    if p1 == price:
        up_count = 0
        down_count = 0
        
    p1 = price#업데이트
if stock1*date[-1]+m1 >= stock2*date[-1]+m2:
    if stock1*date[-1]+m1 == stock2*date[-1]+m2:
        print("SAMESAME")
    else:
        print("BNP")
else:
    print("TIMING")
