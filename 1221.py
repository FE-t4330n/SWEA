# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 테스트 케이스 번호 문자열(tc_str, 예: "#1")과
    #    단어의 총 개수(N)를 입력받아 분리합니다.
    tc_str, N_str = input().split()
    
    # 4. 문자열로 된 숫자("ZRO")를 실제 숫자(0)로 변환할 딕셔너리(mapping)를 만듭니다.
    mapping = {
        "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
        "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
    }
    
    # 5. 정렬된 순서(0~9)대로 단어를 저장한 리스트(num_to_word)를 만듭니다.
    num_to_word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    
    # 6. 0부터 9까지 각 숫자가 몇 번 나왔는지 셀 리스트(counts)를 0으로 초기화합니다.
    counts = [0] * 10
    
    # 7. 정렬할 단어들(words)을 한 줄로 입력받아 공백으로 분리합니다.
    words = input().split()
    
    # 8. 입력받은 단어(words) 리스트를 순회합니다.
    for word in words:
        
        # 9. 단어를 숫자로 변환합니다. (예: "TWO" -> 2)
        num = mapping[word]
        
        # 10. 해당 숫자의 카운트를 1 증가시킵니다. (예: counts[2] += 1)
        counts[num] += 1
            
    # 11. 형식에 맞춰 테스트 케이스 번호(tc_str)를 먼저 출력합니다.
    #     (출력 후 줄바꿈이 아닌 공백을 둡니다)
    print(f"{tc_str}", end=" ")
    
    # 12. 최종 정렬된 결과를 저장할 리스트(result)를 초기화합니다.
    result = []
    
    # 13. 0부터 9까지 순서대로(i) 반복합니다.
    for i in range(10):
        
        # 14. i번째 단어(num_to_word[i])를
        #     i번째 카운트(counts[i]) 만큼 result 리스트에 '확장(extend)'합니다.
        #     (예: "ZRO"를 counts[0]번, "ONE"을 counts[1]번...)
        result.extend([num_to_word[i]] * counts[i])
            
    # 15. 완성된 result 리스트를 공백(' ')으로 묶어(join) 한 줄로 출력합니다.
    print(" ".join(result))