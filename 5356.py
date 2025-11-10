# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 5줄의 문자열을 저장할 리스트(grid)를 초기화합니다.
    grid = []
    
    # 4. 5줄에 걸쳐 문자열을 입력받아 grid 리스트에 추가합니다.
    for _ in range(5):
        grid.append(input())
        
    # 5. 세로로 읽은 결과를 저장할 문자열(result)을 초기화합니다.
    result = ""
    
    # 6. 세로 읽기를 수행합니다. (열(column)을 0부터 14까지 순회)
    #    (문제 제약 조건에서 문자열의 최대 길이는 15입니다)
    for c in range(15): # 0번 열부터 14번 열까지
        
        # 7. 5개의 행(row)을 0부터 4까지 순회합니다.
        for r in range(5): # 0번 행부터 4번 행까지
            
            # 8. [핵심] 현재 행(r)의 문자열 길이(len(grid[r]))가
            #    현재 열(c) 인덱스보다 '큰'지 확인합니다.
            #    (즉, grid[r]에 c번째 글자가 존재하는지 확인)
            if c < len(grid[r]):
                
                # 9. 글자가 존재하면, result에 그 글자(grid[r][c])를 추가합니다.
                result += grid[r][c]
                
    # 10. 모든 세로 읽기가 끝나면, 형식에 맞춰 출력합니다.
    print(f"#{test_case} {result}")