def solution(numbers):
    answer = 0
    for number in range(10): # 0~9까지 숫자 중
        if number not in numbers: # numbers에 없는 숫자
            answer += number
    return answer
