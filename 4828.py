# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N (주어지는 양수의 개수)을 정수로 입력받습니다.
    #    (이 문제에서는 N값을 직접 사용하지 않아도 
    #     max/min 함수로 리스트 전체를 처리할 수 있습니다.)
    N = int(input())
    
    # 4. N개의 양수를 공백으로 구분하여 리스트(numbers)로 저장합니다.
    numbers = list(map(int, input().split()))
    
    # 5. 리스트(numbers)에서 가장 큰 값(max_val)을 찾습니다.
    max_val = max(numbers)
    
    # 6. 리스트(numbers)에서 가장 작은 값(min_val)을 찾습니다.
    min_val = min(numbers)
    
    # 7. (최댓값 - 최솟값)의 차이(result)를 계산합니다.
    result = max_val - min_val
        
    # 8. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")