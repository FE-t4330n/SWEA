# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 달팽이의 크기 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. N x N 크기의 2차원 리스트(grid)를 0으로 초기화합니다.
    #    (0은 아직 방문하지 않은 칸을 의미합니다)
    grid = [[0] * N for _ in range(N)]
    
    # 5. 이동 방향을 시계방향 (우, 하, 좌, 상) 순서로 정의합니다.
    #    dx (행 변화), dy (열 변화)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 6. 현재 위치 (x, y)와 현재 방향 인덱스(dir_idx)를 초기화합니다.
    x, y = 0, 0       # 시작 위치 (0, 0)
    dir_idx = 0       # 0: 오른쪽
    
    # 7. 1부터 N*N 까지의 숫자를 격자에 채웁니다.
    for num in range(1, N * N + 1):
        
        # 8. 현재 위치(x, y)에 현재 숫자(num)를 기록합니다.
        grid[x][y] = num
        
        # 9. 현재 방향(dir_idx)으로 다음 이동할 위치(nx, ny)를 계산합니다.
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]
        
        # 10. 다음 위치(nx, ny)가 격자 범위를 벗어나는지,
        #     혹은 이미 숫자가 채워져 있는지(0이 아닌지) 확인합니다.
        if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] != 0:
            
            # 11-1. 만약 범위를 벗어나거나 이미 채워진 칸이라면,
            #       방향을 시계방향으로 90도 회전시킵니다.
            dir_idx = (dir_idx + 1) % 4
            
            # 11-2. 바뀐 방향으로 다음 위치(nx, ny)를 다시 계산합니다.
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]
            
        # 12. 다음 숫자를 기록할 최종 위치(x, y)를 업데이트합니다.
        x = nx
        y = ny
            
    # 13. 형식에 맞춰 테스트 케이스 번호를 먼저 출력합니다.
    print(f"#{test_case}")
    
    # 14. 완성된 N x N 격자(grid)를 한 행(row)씩 반복하며 출력합니다.
    for row in grid:
        
        # 15. 각 행(row)에 있는 숫자(정수)들을 문자열(str)로 변환한 뒤,
        #     공백(' ')을 기준으로 합쳐서(join) 한 줄로 출력합니다.
        print(' '.join(map(str, row)))