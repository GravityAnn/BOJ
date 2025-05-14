def solution(mats, park):
    answer = -1
    #가장 큰 돗자리 확인
    #지민이가 깔 수 있는 돗자리는 3,3 크기
    ans = [-1]
    
    def seek(x, y):
        
        max_size = -1
        for size_x in mats:
            find = True
            nx = x + size_x
            ny = y + size_x
            if 0 <= nx <= len(park) and 0 <= ny <= len(park[0]):#범위 안에 있다면,
                for i in range(x,nx):
                    for j in range(y,ny):
                        # print(size_x,size_y," : (",i,",",j,") = ",park[i][j])
                        if (park[i][j] != "-1"): #비어있지 않다면
                            find = False
                
                if find == True:
                    max_size = max(size_x, max_size)
                # print("apply?", find,max_size,"\n")
        return max_size
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                ans.append(seek(i, j))
                # print(i, j, ans)
    return max(ans)