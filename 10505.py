# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 사람 수 N을 입력받습니다.
    N = int(input())
    
    # 4. N개의 소득을 리스트로 입력받습니다.
    incomes = list(map(int, input().split()))
    
    # 5. 총합을 구합니다.
    total_sum = sum(incomes)
    
    # 6. 평균을 계산합니다.
    average = total_sum / N
    
    # 7. 평균 이하인 사람의 수를 셀 변수
    count = 0
    
    # 8. 각 소득을 순회
    for income in incomes:
        # 9. 소득이 평균 이하인지 확인
        if income <= average:
            count += 1
            
    # 10. 형식에 맞춰 출력
    print(f"#{test_case} {count}")