# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(숫자 개수), M(이동 횟수)을 입력받음
    N, M = map(int, input().split())
    
    # 4. N개의 숫자를 리스트로 입력받음
    numbers = list(map(int, input().split()))
    
    # 5. M번 이동 후 맨 앞에 올 숫자의 인덱스를 계산
    # (M을 N으로 나눈 나머지)
    final_index = M % N
    
    # 6. 해당 인덱스의 숫자를 출력
    result = numbers[final_index]
    
    print(f"#{test_case} {result}")
