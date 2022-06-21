def solution(s):
    answer = 0 
    dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0} # 영단어 대응지
    
    temp = '' # 임시변수
    ans = '' # 답변변수
    for digit in s:
        if digit.isalpha(): # 문자일 경우 임시변수에 적재
            temp += digit
            if temp in dict.keys(): # 적재된 문자열이 딕셔너리에 있는 값일 경우 숫자로 치환
                ans += str(dict[temp])
                temp = ''
        else:
            ans += str(digit) # 숫자일 경우 답변변수에 적재
            
    answer = int(ans)
    return answer
