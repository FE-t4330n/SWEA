# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. h1, m1, h2, m2 (두 개의 시, 분)를
    #    공백으로 구분하여 정수로 입력받습니다.
    h1, m1, h2, m2 = map(int, input().split())
    
    # 4. 분(minute)을 먼저 계산합니다.
    #    두 분을 더한 값을 60으로 나눈 나머지가 최종 분(final_min)입니다.
    final_min = (m1 + m2) % 60
    
    # 5. 분 계산에서 발생한 '올림 시'(carry_hour)를 계산합니다.
    #    두 분을 더한 값을 60으로 나눈 몫이 올림 시입니다.
    carry_hour = (m1 + m2) // 60
    
    # 6. 시(hour)를 계산합니다.
    #    (h1 + h2 + 올림 시)
    total_hour = h1 + h2 + carry_hour
    
    # 7. 12시간제로 변환합니다.
    #    총 시간을 12로 나눈 나머지를 구합니다.
    final_hour = total_hour % 12
    
    # 8. [예외 처리] 만약 나머지가 0이라면 (12, 24시 등),
    #    12시를 의미하므로 12로 바꿔줍니다.
    if final_hour == 0:
        final_hour = 12
        
    # 9. 형식에 맞춰 테스트 케이스 번호, 최종 시, 최종 분을 출력합니다.
    print(f"#{test_case} {final_hour} {final_min}")