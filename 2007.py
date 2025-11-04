# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 30글자 문자열을 입력받습니다.
    s = input()
    
    # 3. 마디의 길이(L)를 1부터 10까지 순서대로 검사
    for L in range(1, 11):
        
        # 4. L 길이의 '마디 후보' (패턴)
        pattern = s[0:L]
        
        # 5. 그 다음 L 길이의 '다음 조각'
        next_segment = s[L : 2*L]
        
        # 6. 두 조각이 일치하는지 확인
        if pattern == next_segment:
            
            # 7. 일치하면 (가장 짧은 L을 찾았으므로)
            #    결과를 출력하고, 이 테스트 케이스를 종료(break)
            print(f"#{test_case} {L}")
            break