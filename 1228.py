# 1. 총 10개의 테스트 케이스가 주어지므로, 1부터 10까지 반복합니다.
for test_case in range(1, 11):
    
    # 2. 원본 암호문의 길이 N을 정수로 입력받습니다.
    N = int(input())
    
    # 3. 원본 암호문을 공백으로 구분하여 리스트(ciphertext)로 저장합니다.
    ciphertext = list(input().split())
    
    # 4. 명령어의 개수 M을 정수로 입력받습니다.
    M = int(input())
    
    # 5. 전체 명령어 문자열을 공백으로 구분하여 리스트(commands)로 저장합니다.
    commands = list(input().split())
    
    # 6. 명령어 리스트(commands)를 순회할 인덱스(idx)를 0으로 초기화합니다.
    #    (for문이 아닌 while문을 사용하여 명령 길이에 따라 인덱스를 건너뛸 것입니다)
    idx = 0
    
    # 7. 인덱스(idx)가 전체 명령어 리스트의 끝에 도달할 때까지 반복합니다.
    while idx < len(commands):
        
        # 8. 현재 명령어가 'I'(Insert)인지 확인합니다.
        #    (이 문제에서는 'I' 명령어 1개만 제공됩니다)
        if commands[idx] == 'I':
            
            # 9. 'I' 바로 다음의 x (삽입 위치)와 y (삽입 개수)를 정수로 변환하여 읽어옵니다.
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            
            # 10. 삽입할 y개의 숫자들(s)을 [idx+3]부터 [idx+3+y] 전까지 슬라이싱하여
            #     new_nums 리스트로 가져옵니다.
            new_nums = commands[idx + 3 : idx + 3 + y]
            
            # 11. 원본 암호문(ciphertext)의 x번째 인덱스 위치에 new_nums 리스트를 삽입합니다.
            #     (예: L[5:5] = ['a','b'] 는 L 리스트의 5번 인덱스에 'a','b'를 끼워넣습니다)
            ciphertext[x:x] = new_nums
            
            # 12. 현재 처리한 명령어의 총 길이만큼 인덱스를 점프시킵니다.
            #     ('I' 1개 + x 1개 + y 1개 + new_nums(y개) = 총 3 + y 칸)
            idx += (3 + y)
            
        # 13. (만약 'I'가 아닌 다른 명령어가 있을 경우)
        #     다음 명령어를 확인하기 위해 인덱스를 1만 증가시킵니다.
        else:
            idx += 1
            
    # 14. 모든 명령어 처리가 끝난 후, 형식에 맞춰 테스트 케이스 번호를 출력합니다.
    #     (출력 후 줄바꿈 대신 공백을 둡니다)
    print(f"#{test_case}", end=" ")
    
    # 15. 수정된 암호문의 *처음 10개* 항목(ciphertext[:10])만 
    #     공백(' ')으로 묶어(join) 한 줄로 출력합니다.
    print(" ".join(ciphertext[:10]))