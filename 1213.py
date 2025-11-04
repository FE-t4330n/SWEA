# 총 10개의 테스트 케이스가 주어집니다.
for _ in range(10):
    
    # 1. 테스트 케이스 번호를 입력받습니다.
    test_case_num = int(input())
    
    # 2. 찾아야 할 문자열(needle)
    needle = input()
    
    # 3. 검색 대상이 되는 문장(haystack)
    haystack = input()
    
    # 4. count() 함수를 사용해 needle이 haystack에 몇 번 포함되는지 셉니다.
    count = haystack.count(needle)
    
    # 5. 형식에 맞춰 출력
    print(f"#{test_case_num} {count}")