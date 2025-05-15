def solution(bandage, health, attacks):
    answer = 0
    time = 1
    combo = 0
    blood = health
    #붕대감기
    #t 동안 x만큼 회복, 연속으로 하면 y만큼 추가 회복, 최대 체력 존재
    #공격당하면 끊김. 즉시 다시 사용, 0이면 죽음     

    while(time != attacks[len(attacks)-1][0]+1):
        combat = False
        
        for i in range(len(attacks)):
            if attacks[i][0] == time:
                combo = 0
                health -= attacks[i][1]
                combat = True
        if combat == False:
            combo += 1
            health += bandage[1]
            if combo == bandage[0]:
                health += bandage[2]
                combo = 0
            if health > blood:
                health = blood
            
        if health <= 0:
            return -1
        
        time += 1
        print(health)
    return health