# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 정수 N을 입력받습니다.
    N = int(input())
    
    # 4. N의 제곱(N * N)을 계산합니다.
    area = N * N
    
    # 5. 형식에 맞춰 출력
    print(f"#{test_case} {area}")