# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N을 입력받습니다. (10, 20, 30...)
    N = int(input())
    
    # 3. N을 10으로 나눈 몫(n)으로 변환합니다.
    n = N // 10
    
    # 4. DP 테이블(리스트) 생성 (최대 n=30이므로 31 크기)
    dp = [0] * (n + 1)
    
    # 5. 기저 상태(Base Case) 설정
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 3
        
    # 6. 점화식(f(n) = f(n-1) + 2*f(n-2))을 이용해 DP 테이블 채우기
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
        
    # 7. n번째 DP 값(dp[n])을 출력
    print(f"#{test_case} {dp[n]}")