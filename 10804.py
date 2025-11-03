# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. b-d, p-q 변환 딕셔너리(매핑 테이블) 생성
mirror_map = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

for test_case in range(1, T + 1):
    
    # 3. 문자열을 입력받습니다.
    word = input()
    
    # 4. (1단계) 문자열을 뒤집습니다.
    reversed_word = word[::-1]
    
    # 5. (2단계) 뒤집힌 문자열의 각 문자를 딕셔너리로 변환합니다.
    mirrored_result = ""
    for char in reversed_word:
        mirrored_result += mirror_map[char]
        
    # 6. 형식에 맞춰 출력
    print(f"#{test_case} {mirrored_result}")