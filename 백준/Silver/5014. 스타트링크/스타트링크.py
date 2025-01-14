import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)

def bfs(start, goal):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        current_floor, count = queue.popleft()

        if current_floor == goal:
            return count

        for next_floor in (current_floor + u, current_floor - d):
            if 1 <= next_floor <= f and not visited[next_floor]:
                visited[next_floor] = True
                queue.append((next_floor, count + 1))
    return -1

result = bfs(s, g)
if result == -1:
    print("use the stairs")
else:
    print(result)
