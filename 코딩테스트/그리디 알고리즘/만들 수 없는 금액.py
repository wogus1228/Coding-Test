Q. N개의 동전을 가지고 만들 수 없는 양의 정수 금액 중 최솟값을 구하기
  ex) 3원, 5원, 7원짜리 동전을 가지고 있을 경우, 만들 수 없는 최소 정수는 1
  
# 해답
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x :
        break
    target += x

print(target)
