# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 수열의 길이 N을 정수로 입력받습니다.
    N = int(input())
    
    # 4. N개의 숫자가 담긴 수열 P를 리스트로 입력받습니다.
    P = list(map(int, input().split()))
    
    # 5. '평범한 숫자'의 개수를 셀 변수(count)를 0으로 초기화합니다.
    count = 0
    
    # 6. 1번 인덱스부터 N-2번 인덱스(P[1] ~ P[N-2])까지 순회합니다.
    #    (p_i를 확인하기 위해 p_{i-1}, p_i, p_{i+1}이 필요하기 때문입니다)
    for i in range(1, N - 1):
        
        # 7. 세 숫자의 묶음(triplet)을 만듭니다.
        #    (예: P[i-1], P[i], P[i+1])
        triplet = [P[i-1], P[i], P[i+1]]
        
        # 8. 묶음(triplet)을 정렬하여 최솟값과 최댓값을 쉽게 찾도록 합니다.
        #    (예: [1, 3, 2] -> [1, 2, 3])
        triplet.sort()
        
        # 9. 정렬된 리스트에서 최솟값(min_val)은 0번,
        #    최댓값(max_val)은 2번 인덱스에 있습니다.
        min_val = triplet[0]
        max_val = triplet[2]
        
        # 10. 현재 확인하는 숫자 P[i]가
        #     최솟값도 아니고 최댓값도 아닌지 확인합니다.
        #     (즉, 정렬된 리스트의 1번 인덱스 값과 같은지 확인해도 됩니다)
        if P[i] != min_val and P[i] != max_val:
            
            # 11. 위 조건을 만족하면 '평범한 숫자'이므로 count를 1 증가시킵니다.
            count += 1
            
    # 12. 형식에 맞춰 테스트 케이스 번호와
    #     '평범한 숫자'의 총 개수(count)를 출력합니다.
    print(f"#{test_case} {count}")