import math

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 반지름 N을 입력받습니다.
    N = int(input())
    
    # 3. 격자점의 총 개수를 저장할 변수
    count = 0
    N_squared = N * N
    
    # 4. x를 -N부터 N까지(N 포함) 순회합니다.
    for x in range(-N, N + 1):
        
        # 5. y^2 <= N^2 - x^2 를 만족하는 y의 최대값을 찾습니다.
        R_squared = N_squared - (x * x)
        
        # 6. y의 최대 정수값을 계산합니다. (sqrt의 정수 부분)
        max_y = int(math.sqrt(R_squared))
        
        # 7. 가능한 y의 개수(-max_y ~ max_y)는 (2 * max_y + 1)개 입니다.
        count += (2 * max_y + 1)
        
    # 8. 최종 개수를 출력합니다.
    print(f"#{test_case} {count}")