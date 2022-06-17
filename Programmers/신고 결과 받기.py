def solution(id_list, report, k):
    answer = []
    
    receiver_list = {id:0 for id in id_list} # (id, 수신횟수)수신내역 생성
    user_list = {id:0 for id in id_list} # (id, 신고횟수)신고내역 생성
    report = set(report) # 중복 제거(=동일한 신고내역은 1회로 처리)
    
    for receiver in report:
        user_list[receiver.split(' ')[-1]] += 1 # 신고횟수
    
    for receiver in report:
        if user_list[receiver.split(' ')[-1]] >= k: # k번 이상 신고당한 내역 중
            receiver_list[receiver.split(' ')[0]] += 1 # 신고한 이용자의 수신횟수
    
    answer = [value for value in receiver_list.values()]
    
    return answer
