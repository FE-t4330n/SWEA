# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N을 입력받습니다. (N은 리스트의 길이이므로 안 써도 됨)
    N = int(input())
    
    # 3. N개의 숫자를 리스트로 입력받습니다.
    numbers = list(map(int, input().split()))
    
    # 4. 리스트를 오름차순으로 정렬합니다.
    numbers.sort()
    
    # 5. 형식에 맞춰 출력 (*numbers는 리스트 요소를 공백으로 구분)
    print(f"#{test_case}", *numbers)