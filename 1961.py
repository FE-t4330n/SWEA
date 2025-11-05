def rotate_90(grid, N):
    """ N x N 행렬을 90도 시계방향으로 회전시킨 새 행렬을 반환합니다. """
    
    # 1. N x N 크기의 빈 새 행렬을 생성
    new_grid = [[0] * N for _ in range(N)]
    
    # 2. 회전 규칙 적용
    for r in range(N):
        for c in range(N):
            # 원본 [r][c] -> 새 [c][N-1-r]
            new_grid[c][N - 1 - r] = grid[r][c]
            
    return new_grid

# --- 메인 로직 ---

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    # 3. N x N 행렬을 입력받습니다. (예: ['1', '2', '3'])
    grid = [input().split() for _ in range(N)]
    
    # 4. 90도, 180도, 270도 행렬을 각각 계산
    grid_90 = rotate_90(grid, N)
    grid_180 = rotate_90(grid_90, N)
    grid_270 = rotate_90(grid_180, N)
    
    # 5. 형식에 맞춰 출력
    print(f"#{test_case}")
    
    for i in range(N):
        # 6. 각 행렬의 i번째 행을 공백 없이(join) 합쳐서 출력
        str_90 = "".join(grid_90[i])
        str_180 = "".join(grid_180[i])
        str_270 = "".join(grid_270[i])
        
        print(f"{str_90} {str_180} {str_270}")