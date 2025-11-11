# 10개의 테스트 케이스를 처리합니다.
for test_case in range(1, 11):
    # 건물의 개수 N을 입력받습니다.
    N = int(input())
    
    # N개의 건물 높이 정보를 리스트로 입력받습니다.
    buildings = list(map(int, input().split()))
    
    # 해당 테스트 케이스의 총 조망권 세대 수를 저장할 변수
    total_view = 0
    
    # 핵심 로직: 3번째(인덱스 2)부터 N-2번째(인덱스 N-3) 건물까지만 확인
    # 인덱스 0, 1과 N-1, N-2는 양옆 2칸이 비어있으므로 확인할 필요가 없습니다.
    for i in range(2, N - 2):
        
        # 현재 건물의 높이
        current_height = buildings[i]
        
        # 조망권이 0보다 큰 경우에만 (즉, 현재 건물이 0층이 아닐 때)
        if current_height > 0:
            
            # 좌우 2칸씩, 총 4개의 이웃 건물 높이를 리스트로 만듭니다.
            neighbors = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
            
            # 4개의 이웃 중 가장 높은 건물의 높이를 찾습니다.
            max_neighbor = max(neighbors)
            
            # 현재 건물이 이웃 중 가장 높은 건물보다 높다면 조망권이 확보됩니다.
            if current_height > max_neighbor:
                
                # (현재 건물 높이 - 이웃 최고 높이) 만큼 조망권을 더해줍니다.
                view = current_height - max_neighbor
                total_view += view
                
    # 최종 결과 출력
    print(f"#{test_case} {total_view}")