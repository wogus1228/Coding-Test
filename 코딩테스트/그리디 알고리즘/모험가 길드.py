Q. N명의 모험가가 그룹을 구성하는데 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행이 가능
   이때, 최대 몇 개의 그룹을 만들 수 있는가
   ex) N = 5, 각 공포도가 2, 3, 1, 2, 2 일 경우 => 2그룹(2,x | 3,x,x)
   
# 나의 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
temp = 0
cnt = 0

for i in data:
    if(temp != n):
        if(temp <= n):
            temp += i
            cnt += 1
    elif(temp == n):
        break
    
print(cnt)

# 해답
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
