Q. 알파벳 대문자와 숫자로만 구성된 문자열을 알파벳 오름차순으로 정렬하고, 그 뒤에 모든 숫자의 합을 출력
  ex) K1KA5CB7 => ABCKK13

# 나의 풀이
s = input()
result = []
sum = 0

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        result.append(s[i])
    else:
        sum += int(s[i])

result.sort()
print(''.join(result)+str(sum))

# 해답
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
