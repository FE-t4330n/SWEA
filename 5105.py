# 0. 너비 우선 탐색(BFS)을 위한 deque를 가져옵니다.
from collections import deque

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 미로의 크기 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. N x N 크기의 미로(grid)를 입력받습니다.
    #    '13101' 같은 문자열을 [1, 3, 1, 0, 1] 리스트로 변환합니다.
    grid = []
    start_pos = None # (r, c)
    end_pos = None   # (r, c)
    for r in range(N):
        row_str = input()
        row_list = []
        for c in range(N):
            val = int(row_str[c])
            if val == 2:
                start_pos = (r, c)
            elif val == 3:
                end_pos = (r, c)
            row_list.append(val)
        grid.append(row_list)
        
    # 5. 방문 여부 및 거리 계산을 위한 2차원 리스트(visited)를 -1로 초기화합니다.
    #    (-1: 방문 안 함, 0 이상: 출발지로부터의 거리)
    visited = [[-1] * N for _ in range(N)]
    
    # 6. BFS를 위한 큐(queue)를 초기화하고 시작 위치를 넣습니다.
    queue = deque()
    queue.append(start_pos)
    visited[start_pos[0]][start_pos[1]] = 0 # 시작점의 거리는 0
    
    # 7. 상, 하, 좌, 우 4방향 이동을 위한 dx, dy를 정의합니다.
    dr = [-1, 1, 0, 0] # 행(row) 변화
    dc = [0, 0, -1, 1] # 열(col) 변화
    
    # 8. 큐가 빌 때까지 BFS를 수행합니다.
    while queue:
        
        # 9. 큐에서 현재 위치(r, c)를 꺼냅니다.
        r, c = queue.popleft()
        
        # 10. 4방향(d)에 대해 다음 위치(nr, nc)를 탐색합니다.
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 11. [조건 1] 다음 위치가 미로 범위(0 <= nr < N) 안인지 확인합니다.
            if 0 <= nr < N and 0 <= nc < N:
                
                # 12. [조건 2] 다음 위치가 아직 방문하지 않은 곳(-1)인지 확인합니다.
                if visited[nr][nc] == -1:
                    
                    # 13. [조건 3] 다음 위치가 길(0) 또는 도착지(3)인지 확인합니다.
                    if grid[nr][nc] == 0 or grid[nr][nc] == 3:
                        
                        # 14. 조건을 모두 만족하면, 거리를 1 증가시켜 기록하고 큐에 추가합니다.
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))
                        
    # 15. BFS가 끝난 후, 도착지의 거리(final_dist)를 확인합니다.
    final_dist = visited[end_pos[0]][end_pos[1]]
    
    # 16. 최종 결과를 저장할 변수(result)를 0으로 초기화합니다.
    result = 0
    
    # 17. 만약 도착지의 거리가 -1이 아니라면 (도달 가능),
    #     최종 거리는 (도착지까지의 거리 - 1)입니다.
    if final_dist != -1:
        result = final_dist - 1
            
    # 18. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")