Q. 뱀이 맵을 이동하다가 벽 또는 자기 자신의 몸과 부딪히면 게임 끝. 진행 시간을 구하라
   1) 이동한 칸에 사과가 있으면 몸길이 증가
   2) 이동한 칸에 사과가 없으면 몸길이 그대로

# 풀이
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 생성
info = []

# 사과위치 표시
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 방향[동, 남, 서, 북] => 오른쪽을 보고 시작
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 처음 뱀의 위치
    data[x][y] = 2 # 뱀의 위치 표시
    direction = 0 # 처음에는 동쪽
    time = 0 # 진행시간
    index = 0 # 다음 회전 정보
    q = [(x,y)] # 뱀의 위치정보(꼬리가 앞)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        #보드 안에 있고, 몸통이 없는 위치인 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            #사과 없으면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            #사과 있으면 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        #벽이나 몸통과 부딪히는 경우
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        # 회전할 시간인 경우 회전
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
