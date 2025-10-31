# 1. N^M을 계산하는 재귀 함수 정의
def power(base, exponent):
    
    # 2. 기초 단계 (Base Case): M이 0이면 1을 반환
    if exponent == 0:
        return 1
    
    # 3. 재귀 단계 (Recursive Step): N * (N^(M-1))
    else:
        return base * power(base, exponent - 1)

# --- 메인 프로그램 ---

# 총 10개의 테스트 케이스가 주어짐
for _ in range(10):
    
    # 4. 테스트 케이스 번호 입력
    test_case_num = int(input())
    
    # 5. N, M 입력
    N, M = map(int, input().split())
    
    # 6. 재귀 함수 호출
    result = power(N, M)
    
    # 7. 형식에 맞춰 출력
    print(f"#{test_case_num} {result}")