Q. 괴물이 있는 부분은 0, 없는 부분은 1
   (1,1)에서 출발해 오른쪽아래 끝까지 움직여야 하는 최소 칸의 개수
  
# 풀이
from collections import deque

# 맵 크기 입력
n, m = map(int, input().split()) 

# 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향 정의(동,서,남,북)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
# 특정한 노드 방문한 후 거리 입력
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 공간을 넘어선 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 괴물이 없는 경우 거리값 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print(queue)
    # 가장 오른쪽 아래까지의 거리 반환
    print(graph)
    return graph[n - 1][m - 1]

print(bfs(0,0))
