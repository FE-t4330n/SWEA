# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. p와 q를 공백으로 구분하여 실수(float)로 입력받습니다.
    p, q = map(float, input().split())
    
    # 3. 최종 판별 수식 (p > 1 / (2 - q))을 계산합니다.
    if p > (1 / (2 - q)):
        result = "YES"
    else:
        result = "NO"
        
    # 4. 형식에 맞춰 출력합니다.
    print(f"#{test_case} {result}")