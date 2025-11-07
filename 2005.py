# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 파스칼 삼각형의 크기 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. 파스칼 삼각형의 모든 행(row)을 저장할 리스트(triangle)를 초기화합니다.
    triangle = []
    
    # 5. 형식에 맞춰 테스트 케이스 번호를 먼저 출력합니다.
    print(f"#{test_case}")
    
    # 6. N개의 행(i는 0부터 N-1까지)을 만들기 위해 반복합니다.
    for i in range(N):
        
        # 7. 현재 행(current_row)을 1로만 채워서 초기화합니다.
        #    (행의 길이는 행 번호 + 1, 예: 0번째 행은 1개, 3번째 행은 4개)
        current_row = [1] * (i + 1)
        
        # 8. 2번째 행(i=2)부터는 중간 값들을 계산해야 합니다.
        if i > 1:
            # 9. 바로 이전 행(prev_row)을 가져옵니다.
            prev_row = triangle[i-1]
            
            # 10. 현재 행의 중간 값들(j는 1부터 i-1까지)을
            #     이전 행의 값을 참조하여 덮어씁니다.
            for j in range(1, i):
                # (현재 값 = 윗줄 왼쪽 + 윗줄 오른쪽)
                current_row[j] = prev_row[j-1] + prev_row[j]
                
        # 11. 완성된 현재 행(current_row)을 전체 리스트(triangle)에 추가합니다.
        triangle.append(current_row)
        
        # 12. 현재 행의 숫자들을 문자열로 변환하고
        #     공백(' ')으로 묶어(join) 한 줄로 출력합니다.
        print(' '.join(map(str, current_row)))