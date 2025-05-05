import sys
input = sys.stdin.readline

#빙고판
list1 = [list(map(int, input().split())) for _ in range(5)]

#사회자가 부르는 수
list2 = [list(map(int,input().split())) for _ in range(5)]
# print(list2)
def check(list1):
    bingo = 0
    #행
    for i in range(5):#ㅡ
        count_row = 0
        for j in range(5):
            if list1[i][j] == 'O':
                count_row += 1
        if count_row == 5:
            bingo += 1

    # 열
    for j in range(5): #|
        count_col = 0
        for i in range(5):
            if list1[i][j] == 'O':
                count_col += 1
        if count_col == 5:
            bingo += 1

    #대각선
    count3 = 0
    count4 = 0
    for i in range(5):
        if list1[i][i] == 'O': # \
            count3 += 1
        if list1[i][4-i] == 'O': # /
            count4 += 1
    if count3 == 5:
        bingo += 1
    if count4 == 5:
        bingo += 1

    return bingo

count = 0
for i in range(25):
    num = list2[int(i//5)][i%5]
    count += 1
    for j in range(25):
        if num == list1[int(j/5)][j%5]:
            list1[int(j / 5)][j % 5] = 'O'
            break

    if check(list1) >= 3:  # 빙고 3줄 이상
        print(count)
        break




