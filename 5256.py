# 팩토리얼(factorial) 계산을 위해 math 모듈을 가져옵니다.
import math

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. n, a, b를 공백으로 구분하여 정수로 입력받습니다.
    #    (우리는 (x+y)^n 에서 x^a y^b의 계수를 구해야 합니다)
    n, a, b = map(int, input().split())
    
    # 4. 이항 정리에 따라 계수는 n! / (a! * b!) 입니다.
    #    (문제에서 a+b=n이 보장됩니다)
    
    # 5. 분자(numerator)인 n!을 계산합니다.
    numerator = math.factorial(n)
    
    # 6. 분모(denominator)인 (a! * b!)을 계산합니다.
    denominator = math.factorial(a) * math.factorial(b)
    
    # 7. 최종 계수(result)를 정수 나눗셈(//)으로 계산합니다.
    result = numerator // denominator
        
    # 8. 형식에 맞춰 테스트 케이스 번호와 계수(result)를 출력합니다.
    print(f"#{test_case} {result}")