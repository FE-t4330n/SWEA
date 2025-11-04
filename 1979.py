# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N(격자 크기), K(단어 길이)를 입력받습니다.
    N, K = map(int, input().split())
    
    # 3. N x N 격자판을 2차원 리스트로 입력받습니다.
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        
    # 4. K길이 단어가 들어갈 수 있는 총 자리의 수
    total_spots = 0
    
    # --- 5. 가로(행) 검사 ---
    for i in range(N):
        current_length = 0 # 현재 연속된 '1'의 길이
        for j in range(N):
            if grid[i][j] == 1:
                current_length += 1
            else: # 0(벽)을 만났을 때
                if current_length == K:
                    total_spots += 1
                current_length = 0 # 길이 초기화
        
        # (중요) 행이 끝났을 때, 마지막으로 쌓인 길이가 K일 수 있음
        if current_length == K:
            total_spots += 1
            
    # --- 6. 세로(열) 검사 ---
    for j in range(N):
        current_length = 0
        for i in range(N):
            if grid[i][j] == 1:
                current_length += 1
            else: # 0(벽)을 만났을 때
                if current_length == K:
                    total_spots += 1
                current_length = 0
                
        # (중요) 열이 끝났을 때, 마지막으로 쌓인 길이가 K일 수 있음
        if current_length == K:
            total_spots += 1
            
    # 7. 최종 결과 출력
    print(f"#{test_case} {total_spots}")