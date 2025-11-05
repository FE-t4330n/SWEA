# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 명령어의 수 N
    N = int(input())
    
    current_speed = 0
    total_distance = 0
    
    # 3. N개의 명령어를 순서대로 처리
    for _ in range(N):
        command_line = list(map(int, input().split()))
        
        command_type = command_line[0]
        
        if command_type == 1:
            # 4. 가속
            acceleration = command_line[1]
            current_speed += acceleration
        elif command_type == 2:
            # 5. 감속
            deceleration = command_line[1]
            current_speed -= deceleration
            
            # 6. 속도가 0 미만이면 0으로 고정
            if current_speed < 0:
                current_speed = 0
                
        # (command_type == 0 이면 속도 변경 없음)
        
        # 7. 현재 속도로 1초간 이동한 거리를 총 거리에 누적
        total_distance += current_speed
        
    # 8. 최종 결과 출력
    print(f"#{test_case} {total_distance}")