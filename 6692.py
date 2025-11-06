# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 해당 테스트 케이스에서 주어지는 (확률, 월급) 쌍의 개수 N을 입력받습니다.
    N = int(input())
    
    # 4. 월급의 평균(기댓값)을 저장할 변수(expected_salary)를 0.0으로 초기화합니다.
    expected_salary = 0.0
    
    # 5. N개의 (확률, 월급) 쌍을 입력받기 위해 N번 반복합니다.
    for _ in range(N):
        
        # 6. 확률 p (실수)와 월급 x (정수)를 공백으로 구분하여 입력받습니다.
        #    계산을 위해 p와 x를 모두 실수(float)형으로 변환합니다.
        p, x = map(float, input().split())
        
        # 7. 기댓값의 정의(E = Σ(p_i * x_i))에 따라,
        #    (현재 확률 p * 현재 월급 x) 값을 총합에 더합니다.
        expected_salary += (p * x)
            
    # 8. N번의 반복이 끝나면, 계산된 최종 기댓값을 형식에 맞춰 출력합니다.
    #    (샘플 출력과 같이 소수점 6자리까지 표시합니다.)
    print(f"#{test_case} {expected_salary:.6f}")