Q. N * M 크기의 얼음 틀에서 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시.
   구멍이 뚫려있는 부분끼리는 서로 연결된 것으로 간주할 때 구멍에서 생성되는 총 아이스크림의 개수
   ex) 0 0 1 1 0
       0 0 0 1 1 => 3개의 아이스크림 생성
       1 1 1 1 1
       0 0 0 0 0
      
# 해답
# 배열 크기 입력
n, m = map(int, input().split())

# 맵정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

# 특정한 노드 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    # 맵을 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않았으면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상,하,좌,우 재귀 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1
    
print(result)  
