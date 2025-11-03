# 총 10개의 테스트 케이스가 주어집니다.
for test_case in range(1, 11):
    
    # 격자의 크기 N (항상 100)
    N = int(input())
    
    # 100x100 격자판을 입력받습니다.
    # (입력이 공백으로 구분되어 있으므로 split() 사용)
    board = [input().split() for _ in range(N)]
    
    # 총 교착 상태의 개수
    total_deadlocks = 0
    
    # 1. 각 열(j)을 0부터 99까지 순회합니다.
    for j in range(N):
        
        # 2. 'N극(1)이 이동 중인지' 확인하는 플래그
        found_N_pole = False
        
        # 3. 각 열을 위에서 아래로(i) 순회합니다.
        for i in range(N):
            cell = board[i][j]
            
            if cell == '1':
                # N극(1) 발견. 아래로 이동 시작.
                found_N_pole = True
            
            elif cell == '2':
                # S극(2) 발견.
                if found_N_pole:
                    # 만약 이전에 N극이 있었다면, 교착 상태 발생
                    total_deadlocks += 1
                    # 이 N극과 S극은 쌍을 이뤘으므로 플래그 초기화
                    found_N_pole = False
                    
    # 4. 결과 출력
    print(f"#{test_case} {total_deadlocks}")