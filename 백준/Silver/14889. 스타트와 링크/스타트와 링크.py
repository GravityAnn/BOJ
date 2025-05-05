import sys, itertools
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]

def score(team):
    sum = 0
    for i, j in itertools.combinations(team, 2):  # (i,j) 한 번만
        sum += graph[i][j] + graph[j][i]
    return sum

min_num = 10**9
half = n // 2
for team_a in itertools.combinations(people, half):
    team_b = set(people) - set(team_a)

    diff = abs(score(team_a) - score(team_b))
    if diff < min_num:
        min_num = diff

        if min_num == 0:
            break

print(min_num)
