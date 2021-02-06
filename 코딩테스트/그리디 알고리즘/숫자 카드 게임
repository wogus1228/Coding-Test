Q. 숫자 카드 게임
  : 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
    1. 카드는 N * M 행렬 형태
    2. 먼저 뽑고자 하는 카드가 포함되어 있는 행 선택
    3. 선택된 행에 포함된 카드들 중 최소값을 갖는 카드 선택
    4. 이떄 선택되는 최소값들 중 그 값이 최대가 되는 행을 선택
  
  ex) 3 1 2
      4 1 4 => 2
      2 2 2

# 나의 풀이
n, m = map(int, input().split())
max_val = 0

for i in range(n):
    result = list(map(int, input().split()))
    result.sort()
    if(max_val < result[0]):
        max_val = result[0]

print(max_val)

# 해답1
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)
    
print(result)

# 해답2
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(min_value, result)
    
print(result)
