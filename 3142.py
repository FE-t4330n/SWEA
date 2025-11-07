# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 총 뿔의 개수(n)와 총 짐승의 수(m)를
    #    공백으로 구분하여 정수로 입력받습니다.
    n, m = map(int, input().split())
    
    # 4. 연립 방정식을 풉니다.
    #    (1) U + T = m  (짐승의 총합)
    #    (2) U + 2T = n (뿔의 총합)
    #
    #    (2)번 식에서 (1)번 식을 빼면:
    #    (U + 2T) - (U + T) = n - m
    #    T = n - m
    #    따라서 트윈혼(troits)의 수를 먼저 계산합니다.
    troits = n - m
    
    # 5. (1)번 식(U + T = m)을 변형하여
    #    유니콘(unicorns)의 수를 계산합니다. (U = m - T)
    unicorns = m - troits
        
    # 6. 형식에 맞춰 테스트 케이스 번호, 유니콘의 수, 트윈혼의 수를
    #    공백으로 구분하여 출력합니다.
    print(f"#{test_case} {unicorns} {troits}")