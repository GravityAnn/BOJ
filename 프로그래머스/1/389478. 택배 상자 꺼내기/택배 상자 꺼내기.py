def solution(n, w, num):#상자, 한줄, 필요한 상자
    answer = 0
    past = 0
    place = 0
    
    list1 = [0]*(w)
    for i in range(n):
        
        a = i//w
        if a%2 == 1: #홀수
            if (i+1) == num:
                past = list1[(w-1)-(i%w)]
                place = (w-1)-(i%w)
            list1[(w-1)-(i%w)] += 1
            
        else:#짝수
            if (i+1) == num:
                past = list1[i%w]
                place = i%w
            list1[i%w] += 1
            
        
    answer = list1[place] - past
    # print(list1)
    # print(past, place)
    
    return answer