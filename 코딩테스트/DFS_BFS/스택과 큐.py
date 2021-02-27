# 스택
stack = []

stack.append(5)
stack.append(1)
stack.append(2)
stack.pop()

print(stack)
print(stack[::-1]) # 역순 출력

# 큐
# deque : 스택과 큐의 장점을 모두 채택. 데이터 삽입/삭제가 리스트보다 효율적. 
from collections import deque 

queue = deque()

queue.append(5)
queue.append(1)
queue.append(2)
queue.popleft()

print(queue)
queue.reverse() # 역순 정렬
print(queue)
print(list(queue)) # 큐의 리스트화
