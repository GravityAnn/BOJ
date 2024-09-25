import sys
input = sys.stdin.readline

# 식을 입력받습니다.
expression = input().strip()

# '-'를 기준으로 식을 분리합니다.
parts = expression.split('-')

# 첫 번째 부분은 무조건 더합니다.
result = sum(map(int, parts[0].split('+')))

# 이후 부분은 모두 뺍니다.
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

# 결과를 출력합니다.
print(result)
