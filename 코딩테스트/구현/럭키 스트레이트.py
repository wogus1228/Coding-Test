Q. 점수가 특정 조건(자릿수를 기준으로 반으로 나누어 왼쪽 부분의 자릿수합과 오른쪽 부분의 자릿수합이 같을 경우)을 만족할 때 특정한 문자(LUCKY)를 출력하라.
   ex) 123402 => LUCKY, 7755=> READY

# 나의 풀이
n = input()
sum1 = 0
sum2 = 0

for i in range(len(n)):
    if i < len(n)/2:
        sum1 += int(n[i])
    else:
        sum2 += int(n[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
    
# 해답
n = input()
length = len(n)
summary = 0

#왼쪽자리수 합
for i in range(length//2):
    summary += int(n[i])

#오른쪽자리수 합
for i in range(length//2, length):
    summary -= int(n[i])

#결과출력
if summary == 0:
    print("LUCKY")
else:
    print("READY")
   
