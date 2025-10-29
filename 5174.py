from collections import deque

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 간선의 개수 E, 서브트리의 루트 N을 입력받습니다.
    E, N = map(int, input().split())
    
    # 3. E개의 (부모, 자식) 쌍을 리스트로 입력받습니다.
    edge_data = list(map(int, input().split()))
    
    # 4. 인접 리스트를 생성합니다. 
    #    노드 번호는 1부터 E+1까지이므로, E+2 크기로 만듭니다.
    adj_list = [[] for _ in range(E + 2)]
    
    # 5. 인접 리스트에 자식 정보를 채웁니다.
    for i in range(E):
        parent = edge_data[i * 2]
        child = edge_data[i * 2 + 1]
        adj_list[parent].append(child)
        
    # --- BFS(너비 우선 탐색) 시작 ---
    
    # 6. 서브트리의 노드 개수 카운트
    count = 0
    
    # 7. 탐색을 시작할 큐에 루트 노드 N을 넣습니다.
    queue = deque([N])
    
    # 8. 큐가 빌 때까지 반복
    while queue:
        # 9. 큐에서 노드를 하나 꺼냅니다.
        current_node = queue.popleft()
        
        # 10. 노드를 방문했으므로 count 1 증가
        count += 1
        
        # 11. 현재 노드의 모든 자식 노드들을 큐에 추가합니다.
        for child in adj_list[current_node]:
            queue.append(child)
            
    # --- 탐색 종료 ---
    
    # 12. 형식에 맞춰 출력
    print(f"#{test_case} {count}")