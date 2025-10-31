# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N을 입력받습니다. (최대 30)
    N = int(input())
    
    # 3. DP 리스트(배열)를 생성합니다. (N+1 크기)
    dp = [0] * (N + 1)
    
    # 4. 기저 상태(Base Case)를 초기화합니다.
    dp[0] = 1
    if N >= 1:
        dp[1] = 1
    if N >= 2:
        dp[2] = 3
        
    # 5. 3부터 N까지 점화식을 이용해 DP 테이블을 채웁니다.
    for i in range(3, N + 1):
        dp[i] = dp[i-1] + (2 * dp[i-2]) + dp[i-3]
        
    # 6. 최종 결과(dp[N])를 출력합니다.
    print(f"#{test_case} {dp[N]}")