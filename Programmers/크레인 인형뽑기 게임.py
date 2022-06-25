def solution(board, moves):
    answer = 0
    basket = [] # 인형을 담을 바구니
    
    for move in moves: # moves 배열대로 크레인 이동
        for i in range(len(board[0])):
            if board[i][move-1] > 0: # 인형이 존재할 시
                if len(basket) > 0: # 바구니에 든게 있을 경우
                    if basket[-1] == board[i][move-1]: # 가져온 인형이 바구니에 있는 인형과 동일할 시
                        top = basket.pop() # 동일한 인형 제거
                        board[i][move-1] = 0 # 이동된 인형 제거
                        answer += 2 # 사라진 인형 카운트
                    else:    
                        basket.append(board[i][move-1]) # 인형을 바구니로 이동
                        board[i][move-1] = 0 # 이동된 인형 제거
                    break # 인형 이동후 새로 인형 뽑으러 이동
                else: # 바구니에 든게 없으면
                    basket.append(board[i][move-1]) # 인형을 바구니로 이동
                    board[i][move-1] = 0 # 이동된 인형 제거
                break # 인형 이동후 새로 인형 뽑으러 이동
            else:
                continue # 인형이 없을 시 아래칸 인형 확인
                
    return answer
