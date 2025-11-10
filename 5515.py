# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 2016년 각 월의 날짜 수를 리스트(days_in_month)로 정의합니다.
    #    (2016년은 윤년이므로 2월은 29일입니다)
    #    (인덱스 0은 사용하지 않고, 1월이 1번 인덱스가 되도록 합니다)
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 4. 입력받을 월(m)과 일(d)을 공백으로 구분하여 정수로 입력받습니다.
    m, d = map(int, input().split())
    
    # 5. 1월 1일부터 m월 1일 *전*까지의 총 날짜 수(days_before_month)를 계산합니다.
    days_before_month = 0
    for i in range(1, m): # 1월부터 (m-1)월까지 반복
        days_before_month += days_in_month[i]
        
    # 6. 1월 1일부터 m월 d일까지의 총 날짜 수(total_days_from_start)를 계산합니다.
    #    (m월 1일 전까지의 날짜 + m월의 d일)
    total_days_from_start = days_before_month + d
    
    # 7. 기준일(1월 1일)로부터 *며칠이 지났는지*(diff_days) 계산합니다.
    #    (예: 1월 1일은 0일 지남, 1월 2일은 1일 지남)
    diff_days = total_days_from_start - 1
    
    # 8. 기준일(1월 1일)의 요일 인덱스(start_day_index)를 설정합니다.
    #    (문제 출력 기준: 월=0 ... 금=4 ... 일=6)
    start_day_index = 4 # 금요일
    
    # 9. 최종 요일 인덱스(result)를 계산합니다.
    #    (기준 요일 + 지난 날짜 수) % 7
    result = (start_day_index + diff_days) % 7
        
    # 10. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")