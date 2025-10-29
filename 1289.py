# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 목표 메모리 상태(문자열)를 입력받습니다.
    target_memory = input()
    
    # 4. 초기 상태는 '0' (모두 0)이라고 가정
    current_val = '0'
    
    # 5. 수정 횟수
    count = 0
    
    # 6. 목표 메모리를 0번 인덱스부터 순회
    for bit in target_memory:
        
        # 7. 현재 비트가 가정된 상태와 다르다면
        if bit != current_val:
            # 8. 수정을 수행 (count 1 증가)
            count += 1
            # 9. 현재 비트의 값으로 덮어썼으므로, 가정된 상태를 변경
            current_val = bit
            
    # 10. 최종 횟수 출력
    print(f"#{test_case} {count}")