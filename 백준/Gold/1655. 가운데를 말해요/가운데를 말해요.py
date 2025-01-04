import sys, heapq
input = sys.stdin.readline

maxH, minH = [], []
n = int(input())

for _ in range(n):
    num = int(input())
    if not maxH:  # maxH 비어있으면 우선 넣기
        heapq.heappush(maxH, -num)
    else:
        if num <= -maxH[0]:
            heapq.heappush(maxH, -num)
        else:
            heapq.heappush(minH, num)

    # 크기 균형 맞추기
    if len(maxH) > len(minH) + 1:
        val = -heapq.heappop(maxH)
        heapq.heappush(minH, val)
    elif len(minH) > len(maxH):
        val = heapq.heappop(minH)
        heapq.heappush(maxH, -val)

    # 현재 중간값 출력 (짝수 개면 최대 힙 루트가 기준)
    print(-maxH[0])
