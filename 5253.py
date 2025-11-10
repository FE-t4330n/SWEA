# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N과 M의 개수를 입력받습니다.
    N, M = map(int, input().split())
    
    # 4. 'words_to_check' 리스트에 N개의 단어를 입력받습니다.
    words_to_check = []
    for _ in range(N):
        words_to_check.append(input())
        
    # 5. 'prefix_candidates' 리스트에 M개의 단어를 입력받습니다.
    prefix_candidates = []
    for _ in range(M):
        prefix_candidates.append(input())
        
    # 6. 접두어 관계가 성립하는 단어의 개수(count)를 0으로 초기화합니다.
    count = 0
    
    # 7. 'prefix_candidates' 리스트(M개)의 단어(word_b)를 하나씩 확인합니다.
    for word_b in prefix_candidates:

        # 8. 'words_to_check' 리스트(N개)의 단어(word_a)를 하나씩 확인합니다.
        for word_a in words_to_check:

            # 9. [핵심] 만약 word_a가
            #    word_b로 '시작'한다면,
            if word_a.startswith(word_b):

                # 10. count를 1 증가시키고,
                #     이 word_a에 대한 검사는 멈춥니다.
                count += 1
                break 
                
    # 11. 형식에 맞춰 테스트 케이스 번호와 개수(count)를 출력합니다.
    print(f"#{test_case} {count}")