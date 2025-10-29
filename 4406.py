# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 제거할 모음들을 정의하고, 번역 테이블을 *한 번만* 생성합니다.
vowels_to_remove = "aeiou"
# str.maketrans('', '', 'aeiou')는 'a', 'e', 'i', 'o', 'u'를 삭제하는 테이블을 만듭니다.
translation_table = str.maketrans('', '', vowels_to_remove)

# 3. T만큼 반복
for test_case in range(1, T + 1):
    
    # 4. 원본 문자열을 입력받습니다.
    original_string = input()
    
    # 5. translate()를 사용해 모든 모음을 한 번에 제거합니다.
    result_string = original_string.translate(translation_table)
    
    # 6. 결과 출력
    print(f"#{test_case} {result_string}")