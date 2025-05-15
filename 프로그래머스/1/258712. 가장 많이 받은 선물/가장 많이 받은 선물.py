def solution(friends, gifts):
    answer = 0
    graph = [[0]*len(friends) for _ in range(len(friends))]
    
    #다음달 누가 선물을 많이 받을지 예측
    #선물을 주고 받은 기록, 더 많은 선물을 준사람이 받음
    #같거나 없다면, 선물지수가 더 큰사람이 받음
    #선물지수 : 이번달까지 (준 선물 - 받은 선물)#
    #그것마처 같으면 다음달에는 선물 주고받지 않음
    next_month = [0]*len(friends)
    for date in range(len(gifts)):
        g, r = map(str, gifts[date].split())
        graph[friends.index(g)][friends.index(r)] += 1
        
    
    def present(i):
        a = sum(graph[i]) #준거
        b = 0
        for p in range(len(friends)):
            b += graph[p][i]#받은거
        return a - b
            
                
        
        
    for i in range(0, len(friends)):
        for j in range(i+1, len(friends)):
            if (graph[i][j] !=0 or graph[j][i]!= 0): #값이 있는데
                if graph[i][j] != graph[j][i]:#다르다면
                    if graph[i][j] > graph[j][i]:#선물 제공
                        next_month[i] += 1
                    else: 
                        next_month[j] += 1
                    
                else: #같다면,
                    if present(i) > present(j):
                        next_month[i] += 1
                    elif present(i) < present(j):
                        next_month[j] += 1
                    
            else:#값이 없다면,
                if present(i) > present(j):
                        next_month[i] += 1
                elif present(i) < present(j):
                        next_month[j] += 1
                
    print(graph)
    answer = max(next_month)
    print(next_month)
    return answer