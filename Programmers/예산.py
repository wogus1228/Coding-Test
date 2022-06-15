def solution(d, budget):
    answer = 0
    
    d.sort() # 정렬 # 1) sort() : 기존 리스트 변환. 리턴x
                   # 2) sorted() : 정렬된 결과 리턴
    
    for i in d:
        budget -= i # 예산에서 차감
        if budget >= 0: # 예산 존재한다면
            answer += 1 # 지원부서 숫자 증가
            
    return answer
