# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 카드의 개수 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. N개의 카드 이름을 공백으로 구분하여 리스트(cards)로 저장합니다.
    cards = list(input().split())
    
    # 5. 덱을 나눌 기준점(split_index)을 계산합니다.
    #    N이 짝수(예: 6)면 (6+1)//2 = 3
    #    N이 홀수(예: 5)면 (5+1)//2 = 3 (문제의 룰: 홀수면 앞 덱이 한 장 더 많음)
    split_index = (N + 1) // 2
    
    # 6. 계산된 기준점으로 두 개의 덱(deck1, deck2)을 만듭니다.
    #    (예: N=6, [0:3] -> 0,1,2 / [3:] -> 3,4,5)
    #    (예: N=5, [0:3] -> 0,1,2 / [3:] -> 3,4)
    deck1 = cards[:split_index]
    deck2 = cards[split_index:]
    
    # 7. 완벽한 셔플 결과를 저장할 새 리스트(shuffled_deck)를 초기화합니다.
    shuffled_deck = []
    
    # 8. 두 덱의 카드를 번갈아 가며 새 덱에 추가합니다.
    #    (항상 길이가 같거나 더 짧은 deck2의 길이만큼 반복합니다)
    for i in range(len(deck2)):
        # 8-1. 덱 1에서 i번째 카드를 추가합니다.
        shuffled_deck.append(deck1[i])
        # 8-2. 덱 2에서 i번째 카드를 추가합니다.
        shuffled_deck.append(deck2[i])
        
    # 9. 만약 N이 홀수여서 덱 1에 카드가 1장 남아있다면,
    #    (즉, 덱1의 길이가 덱2의 길이보다 깁니다)
    if len(deck1) > len(deck2):
        # 10. 덱 1의 마지막 남은 카드(deck1[-1])를 결과 덱의 맨 뒤에 추가합니다.
        shuffled_deck.append(deck1[-1])
        
    # 11. 형식에 맞춰 테스트 케이스 번호를 출력합니다. (줄바꿈 없이)
    print(f"#{test_case}", end=" ")
    
    # 12. 셔플이 완료된 덱(shuffled_deck)의 모든 카드 이름을
    #     공백(' ')으로 묶어(join) 한 줄로 출력합니다.
    print(" ".join(shuffled_deck))