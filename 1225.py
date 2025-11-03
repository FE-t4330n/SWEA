from collections import deque

# 총 10개의 테스트 케이스
for _ in range(10):
    
    # 1. 테스트 케이스 번호를 입력받습니다.
    tc_num = int(input())
    
    # 2. 8개의 숫자를 deque(큐) 자료구조로 만듭니다.
    queue = deque(map(int, input().split()))
    
    # 3. 1부터 5까지 순환하며 뺄 값을 저장할 변수
    decrement_val = 1
    
    # 4. 종료 조건(0 이하)을 만날 때까지 무한 반복
    while True:
        
        # 5. 큐의 맨 앞에서 숫자를 1개 꺼냅니다.
        num = queue.popleft()
        
        # 6. 뺄 값(decrement_val)만큼 뺍니다.
        num -= decrement_val
        
        # 7. 종료 조건: 0 이하가 되었는지 확인
        if num <= 0:
            # 8. 0으로 값을 고정하고 큐의 맨 뒤에 추가
            queue.append(0)
            # 9. 암호 생성이 끝났으므로 while 루프 탈출
            break
        else:
            # 10. (0보다 큼) 계산된 값을 큐의 맨 뒤에 추가
            queue.append(num)
            
        # 11. 다음 뺄 값을 준비
        decrement_val += 1
        if decrement_val > 5:
            decrement_val = 1 # 1~5 사이클이므로 5 다음은 1
            
    # 12. 최종 큐의 상태를 형식에 맞춰 출력
    #     (*queue는 큐의 모든 요소를 공백으로 구분하여 출력해줍니다)
    print(f"#{tc_num}", *queue)