Q. 게임 캐릭터가 맵 안에서 움직인 칸의 개수를 구하라
   n * m 크기의 직사각형으로, 각각의 칸은 육지 또는 바다.
   캐릭터는 동, 서, 남, 북 중 한 곳을 바라본다.
   캐릭터 움직임 1) 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
              2) 캐릭터의 왼쪽에 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전 후 한 칸 전진
                             가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 하고 1) 재수행
              3) 네 방향 모두 가본 칸이거나 바다로 되어있는 경우 바라보는 방향을 유지한 채 뒤로 한 칸 이동 후 1) 재수행
                 만약, 뒤가 바다라 방향 이동이 불가한 경우 움직임 끝
   방향 : 0 - 북쪽, 1 - 동쪽, 2 - 남쪽, 3 - 서쪽
   맵정보 : 0 - 육지, 1 - 바다 
   ex) 4 * 4 맵, 현재 위치 및 방향 (1, 1, 0) 맵 (1, 1, 1, 1)    -> 3
                                           (1, 0, 0, 1)
                                           (1, 1, 0, 1)
                                           (1, 1, 1, 1)     

# 해답
n, m = map(int, input().split())

# 방문했던 위치를 저장하기 위한 맵
d = [[0] * m for _ in range(n)]
# 현재 위치, 방향
x, y, direction = map(int, input().split())
# 현재 좌표 방문처리
d[x][y] = 1 

# 맵 생성
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 동,서,남,북 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 가보지 않은 칸일 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time += 1
    # 네 방향 다 못 갈 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else :
            break
        turn_time = 0

print(count)
