# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 노드의 총 개수 N을 입력받습니다.
    N = int(input())
    
    # 3. 각 노드 인덱스(1~N)에 어떤 값이 저장될지 기록할 리스트
    #    (0번 인덱스는 사용하지 않음)
    node_values = [0] * (N + 1)
    
    # 4. 방문 순서(저장할 값)를 1부터 N까지 세기 위한 카운터
    counter = 1
    
    # 5. 중위 순회(in-order)를 수행하는 재귀 함수
    def fill_in_order(node_index):
        global counter
        
        # 현재 노드가 N보다 작거나 같을 때만(유효한 노드일 때만)
        if node_index <= N:
            
            # 1. 왼쪽 자식 방문 (2 * node_index)
            fill_in_order(node_index * 2)
            
            # 2. 부모(현재 노드) 방문: 값 할당
            node_values[node_index] = counter
            counter += 1
            
            # 3. 오른쪽 자식 방문 (2 * node_index + 1)
            fill_in_order(node_index * 2 + 1)

    # 6. 루트(1번 노드)부터 중위 순회 시작
    fill_in_order(1)
    
    # 7. 루트(1번)와 N//2번 노드의 값을 찾아 출력
    root_value = node_values[1]
    n_div_2_value = node_values[N // 2]
    
    print(f"#{test_case} {root_value} {n_div_2_value}")