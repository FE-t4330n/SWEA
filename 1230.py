# 총 10개의 테스트 케이스
for test_case in range(1, 11):
    
    N = int(input())
    crypto_list = list(map(int, input().split()))
    M = int(input())
    
    # 1. 모든 명령어를 '한 줄'로 입력받아 '하나의 리스트'로 만듭니다.
    commands = input().split()
    
    # 2. 리스트의 인덱스를 수동으로 조작하며 순회합니다.
    idx = 0 
    
    while idx < len(commands):
        # 3. 현재 인덱스(idx)에서 명령어를 가져옵니다.
        command_type = commands[idx]
        
        if command_type == 'I':
            # I (삽입)
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            # s: (idx+3)부터 (idx+3+y) 전까지
            s = list(map(int, commands[idx + 3 : idx + 3 + y]))
            
            crypto_list[x:x] = s
            
            # 4. 다음 명령어의 시작점으로 인덱스를 점프
            #    (I, x, y, 그리고 s 뭉치(y개) 만큼 이동)
            idx += (3 + y)
            
        elif command_type == 'D':
            # D (삭제)
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            
            del crypto_list[x : x + y]
            
            # (D, x, y 만큼 이동)
            idx += 3
            
        elif command_type == 'A':
            # A (추가)
            y = int(commands[idx + 1])
            # s: (idx+2)부터 (idx+2+y) 전까지
            s = list(map(int, commands[idx + 2 : idx + 2 + y]))
            
            crypto_list.extend(s)
            
            # (A, y, 그리고 s 뭉치(y개) 만큼 이동)
            idx += (2 + y)
            
    # 6. 최종 결과의 앞 10개 항목을 출력
    print(f"#{test_case}", *crypto_list[:10])