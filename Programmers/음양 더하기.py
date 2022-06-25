def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]: # signs[i] 가 참이면 양수
            answer += int(absolutes[i])
        else: # 그렇지 않으면 음수
            answer -= int(absolutes[i])
    return answer
