# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(A의 개수), M(B의 개수)을 입력받음
    N, M = map(int, input().split())
    
    # 4. N개의 숫자를 입력받아 'set_A'를 만듭니다.
    set_A = set(map(int, input().split()))
    
    # 5. M개의 숫자를 입력받아 'set_B'를 만듭니다.
    set_B = set(map(int, input().split()))
    
    # 6. '&' 연산자를 사용해 두 set의 교집합을 구합니다.
    common_set = set_A & set_B
    
    # 7. 교집합의 크기(개수)를 구합니다.
    count = len(common_set)
    
    # 8. 형식에 맞춰 출력
    print(f"#{test_case} {count}")