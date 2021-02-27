from collections import deque

# 도시개수, 도로개수, 거리정보, 출발도시번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도로정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리 0으로 세팅

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
# 최단거리 K인 모든 도시 번호 오름차순 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
# 최단거리 K인 도시 없다면
if check == False:
    print(-1)
