# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 3개의 변의 길이를 입력받습니다.
    a, b, c = map(int, input().split())
    
    # 3. 3개의 숫자를 모두 XOR 연산합니다.
    result = a ^ b ^ c
    
    # 4. 형식에 맞춰 출력
    print(f"#{test_case} {result}")