# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(초기 개수), M(삽입 횟수), L(출력할 인덱스)
    N, M, L = map(int, input().split())
    
    # 4. N개의 숫자를 리스트로 받습니다.
    numbers = list(map(int, input().split()))
    
    # 5. M번 반복 (삽입 연산)
    for _ in range(M):
        # 6. 삽입할 인덱스(idx)와 값(val)을 입력받음
        idx, val = map(int, input().split())
        
        # 7. 리스트의 idx 위치에 val을 삽입
        numbers.insert(idx, val)
        
    # 8. M번의 삽입이 끝난 후, L번 인덱스의 값을 출력
    result = numbers[L]
    
    print(f"#{test_case} {result}")