# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 5명의 점수를 리스트로 입력받습니다.
    scores = list(map(int, input().split()))
    
    # 4. 조정된 점수의 총합을 저장할 변수
    total_sum = 0
    
    # 5. 5명의 점수를 하나씩 확인
    for score in scores:
        
        # 6. 40점 미만인지 확인
        if score < 40:
            # 40점 미만이면 40점을 더함
            total_sum += 40
        else:
            # 40점 이상이면 원래 점수를 더함
            total_sum += score
            
    # 7. 5과목이므로 5로 나눈 몫(평균)을 계산
    average = total_sum // 5
    
    # 8. 형식에 맞춰 출력
    print(f"#{test_case} {average}")