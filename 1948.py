# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 월의 일 수를 리스트로 저장 (0번 인덱스는 0으로 채움)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 3. 1월 1일로부터 며칠째인지 계산하는 함수
def get_day_number(month, day):
    total_days = 0
    # 1월부터 (month-1)월까지의 일 수를 모두 더함
    for m in range(1, month):
        total_days += days_in_month[m]
    # 현재 '일'을 더함
    total_days += day
    return total_days

# 4. T만큼 반복
for test_case in range(1, T + 1):
    
    # 5. 4개의 숫자를 입력받습니다.
    m1, d1, m2, d2 = map(int, input().split())
    
    # 6. 각 날짜의 1/1 기준 일 수를 계산
    start_day = get_day_number(m1, d1)
    end_day = get_day_number(m2, d2)
    
    # 7. (종료일 - 시작일 + 1)을 계산
    result = end_day - start_day + 1
    
    # 8. 형식에 맞춰 출력
    print(f"#{test_case} {result}")