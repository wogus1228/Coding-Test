def solution(participant, completion):
    answer = ''
    parts = {part: 0 for part in participant}
    
    for part in participant:
        if part in parts:
            parts[part] += 1
    
    for comp in completion:
        if comp in parts:
            parts[comp] -= 1
    
    for key, value in parts.items():
        if value != 0:
            answer = key
    
    return answer
