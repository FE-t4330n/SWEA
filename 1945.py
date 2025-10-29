# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N을 입력받습니다.
    N = int(input())
    
    # 4. 소인수분해할 소수 리스트
    primes = [2, 3, 5, 7, 11]
    
    # 5. 각 소인수의 개수(a, b, c, d, e)를 저장할 리스트
    counts = [0] * 5
    
    # 6. primes 리스트를 순회 (i는 0~4, prime은 2, 3, 5, 7, 11)
    for i, prime in enumerate(primes):
        
        # 7. N이 현재 prime으로 나누어지는 동안 반복
        while N % prime == 0:
            
            # 8. 해당 소인수의 카운트를 1 증가
            counts[i] += 1
            # N을 prime으로 나눈 몫으로 갱신
            N //= prime
            
    # 9. counts 리스트를 언패킹(*)하여 출력
    # (예: [1, 3, 2, 2, 3, 1] -> 1 3 2 2 3 1)
    print(f"#{test_case}", *counts)