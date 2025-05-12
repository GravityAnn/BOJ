def solution(schedules, timelogs, startday):
    answer = 0
    #출근시간 자유
    #토, 일은 상관 X
    #상품 받을 직원 수
    person = len(schedules)#사람수
    person_list = [True]*person
    for i in range(7):
        for per in range(person):
            if schedules[per]%100 >= 50:
                time = schedules[per] + 100 -50
                
            else:
                time = schedules[per] + 10
            
            if ((i+startday)%7 != 6 and (i+startday)%7 != 0):
                
                if time < timelogs[per][i]:
                    person_list[per] = False #실패
                    print("실패 : ",schedules[per]+10, timelogs[per][i], (i+startday)%7)
            
    answer = person_list.count(True)
                    

    return answer