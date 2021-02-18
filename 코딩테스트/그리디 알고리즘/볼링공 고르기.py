Q. 두 사람이 총 n개의 볼링공 중 무게가 서로 다른 볼링공을 고르려고 한다. 볼링공마다 무게가 있고, 공의 번호는 순서대로 부여됨
   무게는 1부터 m까지 존재. 두 사람이 고를 수 있는 볼링공 번호의 조합
   ex) n = 5, m = 3, 무게 : [1,3,2,3,2] => (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,4), (4,5)

# 나의 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if(data[i] != data[j]):
            count += 1

print(count)

# 해답
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

print(array)

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
