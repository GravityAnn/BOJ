import sys
input = sys.stdin.readline

N = int(input()) #센서의 개수
K = int(input()) #집중국의 개수
sensor = list(map(int, input().split())) #센서의 위치, 개수는 N
sensor.sort() #순서대로 재배열

arr = []
for distance in range(0, N-1):
    arr.append(sensor[distance+1] - sensor[distance])
arr.sort()

print(sum(arr[:N-K]))

