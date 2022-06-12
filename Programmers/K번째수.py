def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        temp = array[i-1:j] # i부터 j번째까지 배열 잘라 가져오기
        temp.sort() # 배열 정렬
        answer.append(temp[k-1]) # k번째 배열값
    return answer
