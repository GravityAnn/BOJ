def solution(diffs, times, limit):#난이도, 소요리스트, 제산 시한
    answer = 0
    time = 0
    #레벨이 높으면 time_cur을 사용하여 해결
    #레벨이 낮으면 '그 차이'번 틀림.
    #틀릴때마다 time_cur을 사용, time_prev만큼 시간을 사용하여 이전 문제를 풀고 와야함(무조건 품)
    #이후에는 무조건 해결
    
    #숙련도의 최소값을 정수로 return
    start = 1
    end = max(diffs)
        
    while(start <= end):
        limit_time = limit
        limit_time -= times[0]
        
        level = (start + end)//2
        print("레벨:",level, "start:", start, "  end:",end)
        print("")
        
        
        
        for i in range(1, len(diffs)):
            if level >= diffs[i]: #내가 뛰어다다면
                limit_time -= times[i] #그 시간 그대로 소요
            else: #너무 어렵다면
                time = (diffs[i] - level)*(times[i-1] + times[i]) + times[i]
                limit_time -= time
            if limit_time < 0:
                start = level + 1
                print("start를 ",start,"로 이동함")
                break
        if limit_time >= 0:
            end = level - 1
            print("end ",end,"로 이동함")
    print("출력:",level)
    return start