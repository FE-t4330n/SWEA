# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N (전체 배열 크기)과 M (파리채 크기)을
    #    공백으로 구분하여 정수로 입력받습니다.
    N, M = map(int, input().split())
    
    # 4. N x N 크기의 2차원 리스트(grid)를 입력받습니다.
    #    (N줄에 걸쳐서 한 줄씩 list(map(int...))를 실행합니다)
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        
    # 5. 파리채로 잡은 최대 파리 수(max_flies)를 0으로 초기화합니다.
    max_flies = 0
    
    # 6. 파리채가 내려칠 수 있는 모든 시작 위치(r, c)를 순회합니다.
    #    (r, c는 파리채의 '좌측 상단 모서리'를 의미합니다)
    #    (시작점은 0부터 (N-M)까지만 가능합니다. range(N - M + 1) -> 0 ~ N-M)
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            
            # 7. 현재 위치(r, c)에서 M x M 크기 파리채 내부의
            #    파리 수(current_flies)를 0으로 초기화합니다.
            current_flies = 0
            
            # 8. M x M 크기(i, j)만큼 겹쳐서 합을 구합니다.
            for i in range(M):       # 파리채의 행 (0 ~ M-1)
                for j in range(M):   # 파리채의 열 (0 ~ M-1)
                    
                    # 9. 실제 격자(grid)의 위치 (r+i, c+j)에 있는
                    #    파리 수를 현재 합계에 더합니다.
                    current_flies += grid[r + i][c + j]
                    
            # 10. 현재 M x M 영역의 합(current_flies)이
            #     지금까지의 최댓값(max_flies)보다 크면, 최댓값을 갱신합니다.
            if current_flies > max_flies:
                max_flies = current_flies
                
    # 11. 형식에 맞춰 테스트 케이스 번호와 최대 파리 수(max_flies)를 출력합니다.
    print(f"#{test_case} {max_flies}")