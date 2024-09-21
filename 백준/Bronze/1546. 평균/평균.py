import sys
input = sys.stdin.readline

#세준이의 망친 기말점수 조작 프로그램
#자기 점수중 최댓 값 m
#그리고 모두 (점수/M)*100

n = int(input())
score = list(map(int, input().split()))

max_score = max(score)

sum = 0
for i in range(len(score)):
    sum += (score[i]/max_score)*100

print(sum/n)