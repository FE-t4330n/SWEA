def get_tree_node_value(node_num, N_nodes, tree_map):
    """
    재귀적으로 노드의 값을 계산하고, 결과를 tree_map에 저장(메모이제이션)합니다.
    """
    
    # 1. 종료 조건 (값이 이미 저장된 경우): 리프 노드이거나 이미 계산된 상위 노드
    # 이 부분이 중복 계산을 막는 최적화(메모이제이션) 역할을 합니다.
    if node_num in tree_map:
        return tree_map[node_num]
        
    # 2. 종료 조건 (트리 범위 밖): 노드가 N_nodes를 초과하면 존재하지 않는 것으로 보고 0 반환
    if node_num > N_nodes:
        return 0

    # 3. 재귀 호출: 왼쪽 자식과 오른쪽 자식의 값을 합산
    left_child = node_num * 2
    right_child = node_num * 2 + 1

    # 자식 노드의 값 합산
    value = get_tree_node_value(left_child, N_nodes, tree_map) + \
            get_tree_node_value(right_child, N_nodes, tree_map)
    
    # 4. 계산된 값을 딕셔너리에 저장 (메모이제이션)
    tree_map[node_num] = value
    
    return value


# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N_nodes(전체 노드 개수), M_leaves(리프 개수), L_target(구하고자 하는 노드 번호)을 입력받음
    try:
        N_nodes, M_leaves, L_target = map(int, input().split())
    except:
        continue # 입력 오류 시 다음 케이스로

    # 노드 번호와 값이 저장될 딕셔너리
    tree_map = {}
    
    # M개의 리프 노드 값 입력 및 저장
    for i in range(M_leaves):
        try:
            leaf_num, leaf_value = map(int, input().split())
            tree_map[leaf_num] = leaf_value
        except:
            continue # 입력 오류 시 다음 입력으로
    
    # L_target 노드의 값을 계산하고 출력
    result = get_tree_node_value(L_target, N_nodes, tree_map)
    
    print(f'#{test_case} {result}')