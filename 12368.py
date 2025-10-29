# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. A(현재 시각), B(흐른 시간)를 입력받음
    A, B = map(int, input().split())
    
    # 4. (A + B)를 24로 나눈 나머지를 계산
    final_hour = (A + B) % 24
    
    # 5. 형식에 맞춰 출력
    print(f"#{test_case} {final_hour}")