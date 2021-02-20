Q. 8 * 8의 체스판 위에서 나이트가 이동가능한 경우의 수 고르기
   나이트는 1) 수평으로 두 칸 이동한 뒤 수직으로 한 칸, 2) 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동 가능
   체스판의 행의 위치는 1~8, 열의 위치는 a~h로 표현
   ex) 시작위치가 a1 => c2, b3 2가지 경우

# 나의 풀이
point = input()
x1, y1 = 0, 0
count = 0

dx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dy = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(8):
    for j in range(8):
        if dx[i] == point[0] and dy[j] == int(point[1]): # 체스말의 현재 위치
            x1, y1 = i, j # 시작점 기록
            # 수평 두 칸, 수직 한 칸 이동
            i += 2
            j += 1
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            j -= 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            i -= 4
            j += 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            j -= 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            i, j = x1, y1 # 시작점 리셋
            # 수직 두 칸, 수평 한 칸 이동
            j += 2
            i += 1
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            i -= 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            j -= 4
            i += 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1
            i -= 2
            if 0 <= i < 8 and 0 <= j < 8:
                count += 1

print(count)

# 해답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 나이트의 위치 입력받기

# 이동방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#이동가능여부 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
