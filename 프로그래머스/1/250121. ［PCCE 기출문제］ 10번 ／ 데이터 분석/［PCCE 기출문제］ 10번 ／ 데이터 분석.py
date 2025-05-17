def solution(data, ext, val_ext, sort_by):
    #data = [코드번호, 제조일, 최대 수량, 현재 수량]
    #ext = 뽑의 기준
    #val_ext = 기준 정수값
    #sort_by = 기준 문자열
    
    # data에서 ext가 val_ext보다 작은거 골라서 "sort_by로 정렬"
    answer = []
    
    for i in data:
        check = 0
        if ext == "code":
            check = 0
        elif ext == "date":
            check = 1
        elif ext == "maximum":
            check = 2
        elif ext == "remain":
            check = 3
        
        if i[check] <= val_ext:
            answer.append(i)
            
    if sort_by == "code":
        check = 0
    elif sort_by == "date":
        check = 1
    elif sort_by == "maximum":
        check = 2
    elif sort_by == "remain":
        check = 3
    answer.sort(key=lambda x: x[check])
    return answer