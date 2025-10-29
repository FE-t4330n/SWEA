# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N을 입력받습니다.
    N = int(input())
    
    # 4. 누적 합을 저장할 변수
    total_sum = 0
    
    # 5. 1부터 N까지(N 포함) 반복
    for i in range(1, N + 1):
        
        # 6. 홀수인지 짝수인지 판별
        if i % 2 == 1:
            # 홀수이면 더하기
            total_sum += i
        else:
            # 짝수이면 빼기
            total_sum -= i
            
    # 7. 형식에 맞춰 출력
    print(f"#{test_case} {total_sum}")