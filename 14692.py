# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 통나무의 길이 N을 입력받습니다.
    N = int(input())
    
    # 3. N이 짝수인지 홀수인지 판별
    if N % 2 == 0:
        # N이 짝수이면 (N-1)은 홀수 -> 앨리스 승
        winner = "Alice"
    else:
        # N이 홀수이면 (N-1)은 짝수 -> 밥 승
        winner = "Bob"
        
    # 4. 형식에 맞춰 출력
    print(f"#{test_case} {winner}")