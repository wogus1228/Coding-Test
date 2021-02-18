Q. N개의 음식을 차례대로 먹을경우, k초 초 후에 먹을 음식의 순번은?
   각 음식을 먹는 시간은 1초로 동일하며, 다먹은 음식은 제외
   ex) [3,1,2], 5초후 -> 1번 먹을 차례
   
# 나의 해답
food_times = list(map(int, input().split(",")))
k = int(input()) + 1
result = 0

while True :
    for i in range(len(data)):
        if data[i] > 0 :
            data[i] -= 1 #먹은 음식 빼기
            k -= 1       #시간체크
        if k == 0:
            result = i   #먹어야할 음식
            break
    if(k == 0):
        print(result+1)
        break
 
# 풀이
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]

food_times = list(map(int, input().split(",")))
k = int(input())

solution(food_times, k)
