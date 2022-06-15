def solution(nums):
    answer = 0
    uni_nums = set(nums) # 중복 제거
    
    total_cnt = len(uni_nums) # 선택지 개수
    pick_num = len(nums)/2 # 선택할 개수
    
    if total_cnt > pick_num:
        answer = pick_num
    else:
        answer = total_cnt
    
    return answer
