Q. 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 구하라.
   ex) aabbccc => 2a2b3c, ababcdcdababcdcd => 2ab2cd2ab2cd
   
# 해답
s = input()
answer = len(s)

for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step] #앞에서 step만큼의 문자열 추출
    count = 1
    #step 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수 증가
        if prev == s[j:j+step]:
            count += 1
        # 압축 하지 못하는 경우
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step] # 다시 초기화
            count = 1
    # 남아 있는 문자열처리
    compressed += str(count) + prev if count >= 2 else prev
    # 만들어지는 압축 문자열 중 가장 짧은 것
    answer = min(answer, len(compressed))

print(answer)
