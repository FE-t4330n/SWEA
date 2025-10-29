# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N을 입력받습니다.
    N = int(input())
    
    # 4. 본 숫자를 기록할 빈 set
    seen_digits = set()
    
    # 5. 배수 k를 1로 초기화
    k = 1
    
    # 6. set의 크기가 10이 될 때까지 반복
    while len(seen_digits) < 10:
        
        # 7. 현재 숫자 계산
        current_num = N * k
        
        # 8. 숫자를 문자열로 변환
        num_str = str(current_num)
        
        # 9. 문자열의 각 문자를 set에 추가
        for digit_char in num_str:
            seen_digits.add(digit_char)
            
        # 10. (while문 조건이 거짓이면) k를 1 증가시킴
        k += 1
        
    # 11. (while문이 종료됨) 
    #     k가 1 증가된 상태로 종료되므로, 실제 답은 (k-1) * N 입니다.
    #     (또는 current_num 변수에 마지막 값이 저장되어 있습니다.)
    print(f"#{test_case} {current_num}")
