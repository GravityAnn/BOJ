def solution(board, h, w):
    answer = 0
    
    #graph, 칸 위치 -> 이웃한 칸들중 같은 색 칸을 출력하도록
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[h][w] == board[nh][nw]:
                count += 1
        
    answer = count
    return answer