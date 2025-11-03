# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 단어를 입력받습니다.
    word = input()
    
    # 4. 원본 단어와 뒤집은 단어가 같은지 확인
    if word == word[::-1]:
        result = 1
    else:
        result = 0
        
    # 5. 형식에 맞춰 출력
    print(f"#{test_case} {result}")