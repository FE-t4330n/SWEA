# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 작업 신청의 수 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. (시작 시간, 종료 시간) 쌍을 저장할 리스트(activities)를 초기화합니다.
    activities = []
    
    # 5. N개의 줄에 걸쳐 작업 신청(s, e)을 입력받아 리스트에 추가합니다.
    for _ in range(N):
        # (시작 시간 s, 종료 시간 e)
        s, e = map(int, input().split())
        activities.append((s, e))
        
    # 6. 핵심: 활동 리스트를 *종료 시간(e)*을 기준으로 오름차순 정렬합니다.
    #    (lambda 함수의 x는 (s, e) 튜플이며, x[1]은 e를 의미합니다)
    activities.sort(key=lambda x: x[1])
    
    # 7. 선택된 작업의 개수(count)와,
    #    마지막으로 선택된 작업의 종료 시간(last_finish_time)을 초기화합니다.
    count = 0
    last_finish_time = 0
    
    # 8. 종료 시간 순으로 정렬된 작업들을 하나씩 확인합니다.
    for s, e in activities:
        
        # 9. 만약 현재 작업의 시작 시간(s)이
        #    이전에 선택한 작업의 종료 시간(last_finish_time)보다
        #    크거나 같다면, 두 작업은 겹치지 않는 것입니다.
        if s >= last_finish_time:
            
            # 10. 이 작업은 처리가 가능하므로 선택합니다.
            #     count를 1 증가시키고, 마지막 종료 시간을 현재 작업의 e로 업데이트합니다.
            count += 1
            last_finish_time = e
            
    # 11. 형식에 맞춰 테스트 케이스 번호와
    #     최대로 처리 가능한 작업의 수(count)를 출력합니다.
    print(f"#{test_case} {count}")