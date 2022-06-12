import re # 정규표현식

def solution(new_id):
    answer = ''
    # 1단계 소문자 치환
    answer = new_id.lower()
    # 2단계 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
    answer = re.sub(r"[^a-z0-9-_.]", "", answer)
    # 3단계 마침표 2번이상 연속 -> 하나의 마침표 치환
    answer = re.sub('\.+', ".", answer)
    # 4단계 마침표가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')
    # 5단계 빈 문자열이면 a 대입
    if not answer:
        answer += 'a'
    # 6단계 길이 15까지만 자르기
    answer = answer[:15]
    # 제거 후 끝에 마침표 위치시 제거
    answer = answer.rstrip('.')
    # 7단계 길이 2자 이하라면 길이 3이 될때까지 마지막 문자를 붙이기 
    while len(answer) < 3:
        answer += answer[len(answer)-1]
    
    return answer
