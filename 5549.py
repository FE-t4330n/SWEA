# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 100자리의 큰 숫자를 '문자열'로 입력받습니다.
    num_str = input()
    
    # 4. 문자열의 마지막 글자(캐릭터)를 가져옵니다.
    last_char = num_str[-1]
    
    # 5. 마지막 글자 '만' 정수(int)로 변환합니다.
    last_digit = int(last_char)
    
    # 6. 마지막 숫자가 짝수인지 홀수인지 판별
    if last_digit % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
        
    # 7. 형식에 맞춰 출력
    print(f"#{test_case} {result}")