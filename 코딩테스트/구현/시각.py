Q. 특정한 N 시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라
   ex) 00시 00분 03초, 00시 13분 30초...
   
# 풀이
n = int(input()) # 시각
count = 0

for i in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i) + str(m) + str(s):
                count += 1

print(count)
