# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 요일 문자열과 다음 일요일까지 남은 날짜를 매핑하는 딕셔너리
days_map = {
    "SUN": 7,
    "MON": 6,
    "TUE": 5,
    "WED": 4,
    "THU": 3,
    "FRI": 2,
    "SAT": 1
}

# 3. T만큼 반복
for test_case in range(1, T + 1):
    
    # 4. 요일 문자열 S를 입력받습니다.
    S = input()
    
    # 5. 딕셔너리에서 S를 키로 사용하여 값을 찾습니다.
    remaining_days = days_map[S]
    
    # 6. 형식에 맞춰 출력
    print(f"#{test_case} {remaining_days}")