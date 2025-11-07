# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 길이가 4인 문자열 S를 입력받습니다.
    S = input()
    
    # 4. 문자열 S를 알파벳순으로 정렬한 리스트(sorted_S)를 만듭니다.
    #    (예: "ABAB" -> ['A', 'A', 'B', 'B'])
    sorted_S = sorted(S)
    
    # 5. 최종 결과를 저장할 변수(result)를 기본값 "No"로 초기화합니다.
    result = "No"
    
    # 6. 정렬된 리스트가 "AABB" 형태인지 검사합니다.
    #    조건 1: 0번 인덱스와 1번 인덱스가 같고 (A == A)
    #    조건 2: 2번 인덱스와 3번 인덱스가 같고 (B == B)
    #    조건 3: 0번 인덱스와 2번 인덱스가 달라야 함 (A != B)
    if (sorted_S[0] == sorted_S[1] and 
        sorted_S[2] == sorted_S[3] and 
        sorted_S[0] != sorted_S[2]):
        
        # 7. 모든 조건을 만족하면, 결과를 "Yes"로 변경합니다.
        result = "Yes"
        
    # 8. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")