# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. A (현미 빵 가격), B (단호박 빵 가격), C (총 예산)를
    #    공백으로 구분하여 정수로 입력받습니다.
    A, B, C = map(int, input().split())
    
    # 4. 두 빵(A, B) 중에서 더 싼 빵의 가격(min_price)을 찾습니다.
    #    (최대한 많은 빵을 사려면 가장 싼 빵만 사야 합니다)
    min_price = min(A, B)
    
    # 5. 총 예산(C)을 가장 싼 빵의 가격(min_price)으로 나눈
    #    '몫'이 살 수 있는 최대 빵의 개수입니다.
    max_buns = C // min_price
        
    # 6. 형식에 맞춰 테스트 케이스 번호와 최대 빵의 개수(max_buns)를 출력합니다.
    print(f"#{test_case} {max_buns}")