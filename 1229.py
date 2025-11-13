# 1. 총 10개의 테스트 케이스에 대해 반복합니다.
for test_case in range(1, 11):
    
    # 2. 원본 암호문의 길이 N을 입력받습니다.
    N = int(input())
    
    # 3. 원본 암호문을 공백으로 구분하여 리스트(password)로 입력받습니다.
    password = list(input().split())
    
    # 4. 명령어의 개수 M을 입력받습니다.
    M = int(input())
    
    # 5. 전체 명령어 리스트(commands)를 한 줄로 입력받아 리스트로 만듭니다.
    commands = list(input().split())
    
    # 6. 명령어 리스트(commands)를 순회할 인덱스(cursor)를 0으로 초기화합니다.
    #    (명령어마다 길이가 다르므로 for문 대신 while문을 사용합니다)
    cursor = 0
    
    # 7. cursor가 commands 리스트의 끝에 도달할 때까지 while 루프를 실행합니다.
    while cursor < len(commands):
        
        # 8. 현재 커서 위치의 명령어를 'command_type' 변수에 저장합니다. (I 또는 D)
        command_type = commands[cursor]
        
        # 9. 만약 명령어가 'I' (삽입)이라면:
        if command_type == 'I':
            # 10. 삽입 위치(x), 삽입 개수(y)를 정수로 변환하여 읽어옵니다.
            x = int(commands[cursor + 1])
            y = int(commands[cursor + 2])
            
            # 11. 삽입할 숫자들(s)을 (cursor + 3) 위치부터 y개만큼 슬라이싱하여 리스트로 만듭니다.
            s = commands[cursor + 3 : cursor + 3 + y]
            
            # 12. [핵심] password 리스트의 x번 인덱스 위치에 s 리스트를 통째로 삽입합니다.
            password[x:x] = s
            
            # 13. cursor를 (I, x, y, ...s)를 모두 건너뛴 다음 명령어 위치로 이동시킵니다. (총 3 + y 칸)
            cursor += (3 + y)
            
        # 14. 만약 명령어가 'D' (삭제)라면:
        elif command_type == 'D':
            # 15. 삭제 위치(x), 삭제 개수(y)를 정수로 변환하여 읽어옵니다.
            x = int(commands[cursor + 1])
            y = int(commands[cursor + 2])
            
            # 16. [핵심] password 리스트의 x번 인덱스부터 y개의 원소를 삭제합니다.
            del password[x : x + y]
            
            # 17. cursor를 (D, x, y)를 모두 건너뛴 다음 명령어 위치로 이동시킵니다. (총 3 칸)
            cursor += 3
    
    # 18. 모든 명령어 처리가 끝난 후, 형식에 맞춰 테스트 케이스 번호를 출력합니다.
    print(f"#{test_case}", end=" ")
    
    # 19. 수정된 암호문의 맨 앞 10개만 슬라이싱하여 공백으로 구분해 출력합니다.
    print(" ".join(password[:10]))