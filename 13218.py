# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 학생 수 N을 입력받습니다.
    N = int(input())
    
    # 4. N을 3으로 나눈 몫(정수 나눗셈)을 계산
    max_groups = N // 3
    
    # 5. 형식에 맞춰 출력
    print(f"#{test_case} {max_groups}")