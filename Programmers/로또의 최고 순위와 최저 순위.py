def solution(lottos, win_nums):
    answer = []
    rank = [1, 2, 3, 4, 5, 6] # 로또 등수 배열
    match_cnt = 0 # 매칭 개수
    zero_cnt = 0 # 0 표기 개수
    
    for i in lottos:
        if i == 0: # 0 개수 확인
            zero_cnt +=1
        elif i in win_nums: # 매칭 개수 확인
            match_cnt+=1
        
    min_result = match_cnt          # 최저 순위
    max_result = match_cnt+zero_cnt # 최고 순위
    
    if min_result == 0: # 0개는 1개와 같은 결과
        min_result += 1
    if max_result == 0: # 0개는 1개와 같은 결과
        max_result += 1
    
    answer.append(rank[-max_result])
    answer.append(rank[-min_result])
    
    return answer
