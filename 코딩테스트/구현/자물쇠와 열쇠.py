Q. N*N 의 자물쇠를 m*m의 열쇠를 이용해 열 수 있으면 True, 없으면 False를 return 하기

# 풀이
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)    # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0] * n for _ in range(m)] #결과
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
    return result

# 자물쇠 중간부분 모두 1인치 체크
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 맞는지 확인
                if check(new_lock) == True:
                    return True
                # 자물쇠 열쇠 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)
