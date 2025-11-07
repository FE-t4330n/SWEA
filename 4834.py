# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 카드의 장수 N을 정수로 입력받습니다.
    #    (이 문제에서는 N값을 직접 사용하지는 않지만, 입력을 받아야 합니다)
    N = int(input())
    
    # 4. N개의 숫자가 공백 없이 이어진 문자열(card_str)을 입력받습니다.
    card_str = input()
    
    # 5. 0부터 9까지 각 숫자의 개수를 저장할 리스트(counts)를 0으로 초기화합니다.
    #    (counts[0]은 0의 개수, counts[9]는 9의 개수)
    counts = [0] * 10
    
    # 6. 입력받은 카드 문자열(card_str)을 한 글자씩 순회합니다.
    for char in card_str:
        
        # 7. 현재 글자(char)를 정수(digit)로 변환합니다. (예: '4' -> 4)
        digit = int(char)
        
        # 8. counts 리스트의 해당 숫자(digit) 인덱스 값을 1 증가시킵니다.
        counts[digit] += 1
        
    # 9. 가장 많은 카드의 숫자(max_digit)와 그 개수(max_count)를
    #    찾기 위한 변수를 초기화합니다.
    max_count = -1  # 0개인 카드도 있으므로, 0보다 작은 -1로 초기화
    max_digit = 0
    
    # 10. 0번 숫자부터 9번 숫자까지(i) 순회하며 counts 리스트를 확인합니다.
    for i in range(10):
        
        # 11. 만약 현재 숫자(i)의 개수(counts[i])가
        #     지금까지의 최대 개수(max_count)보다 '크거나 같다'면 (>=),
        #     (장수가 같을 땐 숫자가 큰 쪽이 이기므로, '=' 조건이 중요합니다)
        if counts[i] >= max_count:
            
            # 12. 최대 개수(max_count)와 최대 숫자(max_digit)를
            #     현재 값(counts[i])과 현재 숫자(i)로 업데이트합니다.
            max_count = counts[i]
            max_digit = i
            
    # 13. 형식에 맞춰 테스트 케이스 번호,
    #     최대 숫자(max_digit), 최대 개수(max_count)를 출력합니다.
    print(f"#{test_case} {max_digit} {max_count}")