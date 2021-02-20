Q. 크기 n인 지도에서 계획서에 적힌 L(왼쪽), R(오른쪽), U(위), D(아래)에 따라 이동했을 때 좌표 구하기. 시작 좌표는 1, 1
   ex) n=5, R R R U D D => (3,4)
   
#나의 풀이
n = int(input()) # 공간의 크기
root = list(input().split()) # 이동계획
point_x = 1
point_y = 1

for i in root:
    if i == 'R':
        if point_y < n:
            point_y += 1
    elif i == 'L':
        if point_y > 1 and point_y < n:
            point_y -= 1
    elif i == 'U':
        if point_x > 1 and point_x < n:
            point_x -= 1
    elif i == 'D':
        if point_x < n:
            point_x += 1

print(point_x, point_y)

# 해답
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            print(plan, move_types[i], dx[i], dy[i])
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
