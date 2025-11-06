# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N (총 꽃의 개수)과 D (분무기 범위)를 
    #    공백으로 구분하여 정수(int)로 입력받습니다.
    N, D = map(int, input().split())
    
    # 4. 하나의 분무기가 덮을 수 있는 꽃의 최대 개수를 계산합니다.
    #    (범위가 [x-D, x+D]이므로 총 길이는 2*D + 1 입니다)
    coverage = (2 * D) + 1
    
    # 5. 필요한 최소 분무기 개수를 계산합니다.
    #    (총 꽃의 개수 N) / (분무기 1개당 범위 coverage)의 결과를
    #    '올림' 처리합니다.
    #    (A + B - 1) // B 는 math.ceil(A / B)와 같은 올림 연산입니다.
    min_sprinklers = (N + coverage - 1) // coverage
            
    # 6. 형식에 맞춰 테스트 케이스 번호와 최소 분무기 개수를 출력합니다.
    print(f"#{test_case} {min_sprinklers}")