import sys

input = sys.stdin.readline
n, m = map(int, input().split()) #못듣, 못본

#못 들은 사람
li = set()
for _ in range(n):
    li.add(input().strip())

group = []
cnt = 0

    # 못 본 사람
for i in range(m):
    sep = input().strip()
    if sep in li:
        cnt += 1
        sep = sep.strip()
        group.append(sep)
group.sort()
print(cnt)
for name in group:
    print(name)
