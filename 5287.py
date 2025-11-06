# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 초기 온도 T, 종료 온도 T_end, 냉각 계수 k를 
    #    공백으로 구분하여 실수(float)로 입력받습니다.
    #    (테스트 케이스 T와 구분하기 위해 변수명을 T_val로 사용합니다.)
    T_val, T_end, k = map(float, input().split())
    
    # 4. cost() 함수 호출 횟수를 저장할 변수(count)를 0으로 초기화합니다.
    count = 0
    
    # 5. 현재 온도(T_val)가 종료 온도(T_end)보다 큰 동안 반복합니다.
    while T_val > T_end:
        
        # 6. 루프가 한 번 실행될 때마다 cost()가 호출된 것이므로
        #    count를 1 증가시킵니다.
        count += 1
        
        # 7. 현재 온도를 T_val * k 값으로 업데이트(냉각)합니다.
        T_val *= k
            
    # 8. 형식에 맞춰 테스트 케이스 번호와 최종 횟수(count)를 출력합니다.
    print(f"#{test_case} {count}")