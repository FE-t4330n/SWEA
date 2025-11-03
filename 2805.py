# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 농장의 크기 N
    N = int(input())
    
    # 3. N x N 격자판을 입력받습니다.
    #    '02032' 같은 문자열로 입력되므로, 
    #    각 문자를 int로 변환해 2차원 리스트로 만듭니다.
    grid = []
    for _ in range(N):
        row_str = input()
        grid.append([int(char) for char in row_str])
        
    # 4. 총 수익
    total_profit = 0
    
    # 5. 가운데 인덱스와, 현재 행의 너비(반지름)
    center = N // 2
    width = 0
    
    # 6. 모든 행(i)을 0부터 N-1까지 순회
    for i in range(N):
        
        # 7. 수확할 열의 시작점과 끝점 계산
        start_col = center - width
        end_col = center + width
        
        # 8. 해당 범위의 농작물 가치를 모두 더함
        for j in range(start_col, end_col + 1):
            total_profit += grid[i][j]
            
        # 9. 너비(width) 갱신
        if i < center:
            # 상단부: 너비 1 증가
            width += 1
        else:
            # 하단부 (가운데 포함): 너비 1 감소
            width -= 1
            
    # 10. 최종 결과 출력
    print(f"#{test_case} {total_profit}")