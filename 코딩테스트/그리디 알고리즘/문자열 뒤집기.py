Q. 0과 1로만 이루어진 문자열 S에 대해, 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
   이떄 모두 같은 숫자를 만들 수 있는 최소 횟수는?
   ex) 0001100 -> 1110011 -> 1111111(2번) / 0001100 -> 0000000(1번) => 최소 1번

# 나의 풀이
data = input()
check_bit = data[0]
count = 0

for i in range(1, len(data)):
    if(check_bit != data[i]):
        if(data[i] != data[i-1]):
            count += 1

print(count)

# 해답
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
   
 
