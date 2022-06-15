def solution(participant, completion):
    answer = ''
    parts = {part: 0 for part in participant} # 딕셔너리 생성
    
    for part in participant:
        if part in parts:
            parts[part] += 1 # 참가자 명단에 존재할 시 체크
    
    for comp in completion:
        if comp in parts:
            parts[comp] -= 1 # 완주자 명단에 존재할 시 체크
    
    for key, value in parts.items():
        if value != 0: # 체크안된 대상 확인
            answer = key 
    
    return answer
