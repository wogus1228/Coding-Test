def solution(a, b):
    answer = 1234567890
    temp = []
    
    temp = [a[i]*b[i] for i in range(len(a))] # 두 리스트를 곱한 리스트 생성
    
    answer = sum(temp) # 리스트 모든 원소 합
    
    return answer
