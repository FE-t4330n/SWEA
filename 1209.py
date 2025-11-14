# 1. 총 10개의 테스트 케이스가 주어지므로 10번 반복합니다.
for _ in range(10):
    
    # 2. 테스트 케이스 번호(tc_num)를 입력받습니다.
    tc_num = int(input())
    
    # 3. 100x100 크기의 2차원 배열(board)을 입력받습니다.
    #    (100줄에 걸쳐 각 줄에 100개의 숫자가 들어옵니다)
    board = []
    for _ in range(100):
        row = list(map(int, input().split()))
        board.append(row)
        
    # 4. 전체 합계 중 최댓값을 저장할 변수(max_total_sum)를 0으로 초기화합니다.
    max_total_sum = 0
    
    # 5. 두 대각선의 합계를 저장할 변수(diag1_sum, diag2_sum)를 0으로 초기화합니다.
    diag1_sum = 0  # 좌상 -> 우하 ( \ )
    diag2_sum = 0  # 우상 -> 좌하 ( / )
    
    # 6. 100개의 행과 열을 순회합니다. (i는 0부터 99까지)
    for i in range(100):
        
        # 7. i번째 행의 합(row_sum)과 i번째 열의 합(col_sum)을 0으로 초기화합니다.
        row_sum = 0
        col_sum = 0
        
        # 8. i번째 행/열 내부의 100개 원소를 순회합니다. (j는 0부터 99까지)
        for j in range(100):
            # 9. i번째 행의 합을 구합니다. (행 인덱스 i는 고정, 열 j가 0~99)
            row_sum += board[i][j]
            # 10. i번째 열의 합을 구합니다. (열 인덱스 i는 고정, 행 j가 0~99)
            col_sum += board[j][i]
            
        # 11. i번째 행의 합과 열의 합 계산이 끝나면,
        #     현재까지의 최댓값(max_total_sum)과 이 두 합을 비교하여
        #     가장 큰 값으로 갱신합니다.
        max_total_sum = max(max_total_sum, row_sum, col_sum)
        
        # 12. 두 대각선의 합을 누적합니다.
        # (좌상 -> 우하 대각선은 [i][i] 위치의 원소입니다)
        diag1_sum += board[i][i]
        # (우상 -> 좌하 대각선은 [i][99-i] 위치의 원소입니다)
        diag2_sum += board[i][99 - i]
        
    # 13. 모든 행/열의 합계 비교가 끝난 후,
    #     최종적으로 두 대각선의 합(diag1_sum, diag2_sum)과도 비교하여
    #     전체 최댓값을 갱신합니다.
    max_total_sum = max(max_total_sum, diag1_sum, diag2_sum)
    
    # 14. 형식에 맞춰 테스트 케이스 번호와 계산된 최댓값을 출력합니다.
    print(f"#{tc_num} {max_total_sum}")