# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(A의 단어 수), M(B의 단어 수)을 입력받음
    N, M = map(int, input().split())
    
    # 4. N개의 단어를 입력받아 set_A를 만듭니다.
    #    (set comprehension: N번 반복하며 input()을 받아 set에 자동 저장)
    set_A = {input() for _ in range(N)}
    
    # 5. M개의 단어를 입력받아 set_B를 만듭니다.
    set_B = {input() for _ in range(M)}
    
    # 6. '&' 연산자를 사용해 두 set의 교집합을 구합니다.
    common_words_set = set_A & set_B
    
    # 7. 교집합의 크기(개수)를 구합니다.
    count = len(common_words_set)
    
    # 8. 형식에 맞춰 출력
    print(f"#{test_case} {count}")