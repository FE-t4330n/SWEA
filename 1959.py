# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N(A의 길이), M(B의 길이)을 입력받습니다.
    N, M = map(int, input().split())
    
    # 3. 배열 A와 B를 입력받습니다.
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 4. A와 B 중 어느 것이 더 짧은지 확인합니다.
    if N <= M:
        shorter = A
        longer = B
    else:
        shorter = B
        longer = A
        
    # 5. 최대값을 저장할 변수를 매우 작은 값으로 초기화합니다.
    max_product = -float('inf')
    
    # 6. '더 짧은 배열'을 '더 긴 배열' 위에서 한 칸씩(i) 이동시킵니다.
    #    총 (긴 길이 - 짧은 길이 + 1)번 이동합니다.
    for i in range(len(longer) - len(shorter) + 1):
        
        current_product = 0
        
        # 7. 현재 위치에서 마주 보는 값들의 곱의 합을 구합니다.
        for j in range(len(shorter)):
            current_product += shorter[j] * longer[i + j]
            
        # 8. 최대값을 갱신합니다.
        max_product = max(max_product, current_product)
        
    # 9. 최종 결과를 출력합니다.
    print(f"#{test_case} {max_product}")