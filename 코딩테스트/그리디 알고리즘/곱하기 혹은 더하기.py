Q. 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 숫자 사이에 '+' 혹은 '*' 숫자를 넣어 결과적으로 만들어 질 수 있는 가장 큰 수를 구하라.
  ex) 02984 => (((0+2)*9)*8)*4
  
# 나의 풀이
s = input()
result = 0

for index, value in enumerate(s):
    if(index == 0):
        result += int(value)
    else:
        if(int(value) <= 1 or result <= 1):
            result += int(value)
        else:
            result *= int(value)
            
print (result)

# 해답
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
