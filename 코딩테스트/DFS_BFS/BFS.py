from collections import deque

# bfs 정의
def bfs(graph, start, visited):
    # deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드정보 2차원 리스트로 입력
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문정보 초기화
visited = [False] * 9

bfs(graph, 1, visited)
