# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    try:
        str1 = input()
        str2 = input()
    except:
        break

    # 1. str1의 문자를 빠르게 찾기 위해 Set을 사용합니다. (O(|S1|))
    #    (이 부분은 딕셔너리에 미리 카운팅을 하는 대신, str1에 포함된 문자만 걸러내는 용도로 사용)
    str1_chars = set(str1)

    # 2. str1의 각 문자가 str2에 몇 번 나오는지 저장할 딕셔너리를 초기화합니다.
    #    str1에 있는 문자로만 Key를 구성하고, Value는 0으로 초기화합니다.
    count_map = {char: 0 for char in str1_chars}

    # 3. str2를 단 한 번만 순회합니다. (O(|S2|))
    for char2 in str2:
        # 현재 문자가 str1에 포함되어 있는지 (즉, count_map의 키인지) O(1) 시간에 확인
        if char2 in count_map:
            count_map[char2] += 1
            
    # 4. 딕셔너리에서 가장 큰 Value(카운트)를 찾습니다.
    #    count_map이 비어있을 경우 (str1이 빈 문자열일 경우)를 대비해 default=0을 사용합니다.
    #    O(|S1|) - 딕셔너리의 크기만큼 순회합니다.
    if count_map:
        max_count = max(count_map.values())
    else:
        max_count = 0 # str1이 비어있으면 0

    print(f"#{test_case} {max_count}")