# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. A, B를 입력받습니다.
    A, B = map(int, input().split())
    
    result = 0
    
    # 4. A와 B가 모두 9 이하인지 확인
    if A <= 9 and B <= 9:
        # 5. (참) 곱셈 결과를 저장
        result = A * B
    else:
        # 6. (거짓) -1을 저장
        result = -1
        
    # 7. 형식에 맞춰 출력
    print(f"#{test_case} {result}")