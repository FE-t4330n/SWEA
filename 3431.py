# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. L(최소), U(최대), X(현재)를 입력받음
    L, U, X = map(int, input().split())
    
    result = 0
    
    # 4. 초과한 경우
    if X > U:
        result = -1
    # 5. 부족한 경우
    elif X < L:
        result = L - X
    # 6. 적정한 경우 (L <= X <= U)
    else:
        result = 0
        
    # 형식에 맞춰 출력
    print(f"#{test_case} {result}")