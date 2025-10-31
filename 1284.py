# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. P, Q, R, S, W를 한 줄에 입력받습니다.
    P, Q, R, S, W = map(int, input().split())
    
    # 3. A사 요금 계산
    cost_a = P * W
    
    # 4. B사 요금 계산
    cost_b = 0
    if W <= R:
        # (경우 1) 사용량이 R 이하일 때
        cost_b = Q
    else:
        # (경우 2) 사용량이 R 초과일 때
        cost_b = Q + (W - R) * S
        
    # 5. 두 요금 중 더 저렴한 값을 찾습니다.
    result = min(cost_a, cost_b)
    
    # 6. 형식에 맞춰 출력
    print(f"#{test_case} {result}")