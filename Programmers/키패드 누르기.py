def distance(x1, y1, x2, y2): # 맨하탄 거리측정 함수
    distance = 0
    a = abs(x2-x1)
    b = abs(y2-y1)
    distance = a+b 
    return distance 

def solution(numbers, hand):
    num_array = [[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
                ['*', 0, '#']] # 키패드
    answer = ''
    l_x, l_y = 3, 0 # *에서 시작
    r_x, r_y = 3, 2 # #에서 시작
    
    for number in numbers:
        for i in range(4):
            for j in range(3):
                if number == num_array[i][j]:
                    if j == 0: # 왼쪽 1,4,7은 왼쪽
                        answer += 'L'
                        l_x, l_y = i, j # 왼쪽 손가락 위치 저장
                    elif j == 2: # 오른쪽 3,6,9은 왼쪽
                        answer += 'R'
                        r_x, r_y = i, j # 오른쪽 손가락 위치 저장
                    else:
                        if distance(l_x, l_y, i, j) == distance(r_x, r_y, i, j): # 거리가 동일한 경우 주사용 손으로
                            answer += hand[0].upper()
                            if hand[0].upper() == 'L':
                                l_x, l_y = i, j
                            else:
                                r_x, r_y = i, j
                        elif distance(l_x, l_y, i, j) > distance(r_x, r_y, i, j):
                            answer += 'R'
                            r_x, r_y = i, j
                        else:
                            answer += 'L'
                            l_x, l_y = i, j
    return answer
