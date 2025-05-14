def solution(wallet, bill):
    #지페 접는다. 
    #긴쪽을 반으로 접는다.
    #소수점은 버린다.
    #90도 돌려서라도 넣을 수 있으면 그만 접는다. 
    answer = 0
    
    while (min(bill) > min(wallet)) or (max(bill) > max(wallet)):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    
    return answer