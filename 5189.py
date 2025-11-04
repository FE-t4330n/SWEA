# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 구역의 수 N
    N = int(input())
    
    # 3. N x N 배터리 소모량 그리드 (0-indexed로 사용)
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        
    # 4. 방문 여부를 기록 (0-indexed)
    visited = [False] * N
    
    # 5. 최소 소모량을 저장할 변수 (최대값으로 초기화)
    min_cost = float('inf')
    
    # 6. 백트래킹(DFS) 함수 정의
    # (현재 노드, 방문한 노드 수, 현재까지의 비용)
    def dfs(current_node, num_visited, current_cost):
        global min_cost
        
        # 7. 가지치기: 현재 비용이 이미 최소 비용보다 크면 중단
        if current_cost >= min_cost:
            return
            
        # 8. Base Case: N개의 모든 구역을 다 방문했다면
        if num_visited == N:
            # 사무실(0)로 돌아가는 비용을 추가
            total_cost = current_cost + grid[current_node][0]
            # 최소값 갱신
            min_cost = min(min_cost, total_cost)
            return
            
        # 9. Recursive Step: 다음 구역(next_node) 탐색
        for next_node in range(N):
            if not visited[next_node]:
                # 방문 처리
                visited[next_node] = True
                
                # 다음 노드로 이동 (비용 누적)
                dfs(next_node, num_visited + 1, current_cost + grid[current_node][next_node])
                
                # 백트래킹: 다음 경로 탐색을 위해 방문 기록 되돌리기
                visited[next_node] = False

    # --- 탐색 시작 ---
    
    # 10. 사무실(0번 노드)에서 시작
    visited[0] = True
    dfs(0, 1, 0)
    
    # 11. 최종 결과 출력
    print(f"#{test_case} {min_cost}")