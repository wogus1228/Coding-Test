Q. 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행.
   단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능
   1. N에서 1을 뺀다.
   2. N을 K로 나눈다.
   
   ex) N = 17, K = 4 => 3번(-1 /4 /4) 
   
# 나의 풀이
n, k = map(int, input().split())
cnt = 0

while n > 1:
    if n%k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

# 해답1
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# 해답2
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k
    print(n, k, result)
    
result += (n-1)
print(result)
