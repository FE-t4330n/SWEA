# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N (전체 정수 개수)과 M (구간의 크기)을
    #    공백으로 구분하여 정수로 입력받습니다.
    N, M = map(int, input().split())
    
    # 4. N개의 정수가 담긴 리스트(a)를 입력받습니다.
    a = list(map(int, input().split()))
    
    # 5. M개씩 묶은 구간 합들을 저장할 리스트(sums_list)를 초기화합니다.
    sums_list = []
    
    # 6. M개 묶음(구간)이 시작될 수 있는 모든 인덱스(i)에 대해 반복합니다.
    #    (첫 묶음의 시작 인덱스 0부터,
    #     마지막 묶음의 시작 인덱스 N-M 까지 반복)
    #    (range(N - M + 1)은 0부터 N-M까지를 의미합니다)
    for i in range(N - M + 1):
        
        # 7. 현재 인덱스(i)부터 M개의 숫자(a[i] ~ a[i+M-1])를
        #    슬라이싱하여 그 합(current_sum)을 구합니다.
        #    (예: N=5, M=3일 때 i=0이면 a[0:3] -> 1,2,3 합)
        current_sum = sum(a[i : i + M])
        
        # 8. 계산된 구간 합을 리스트(sums_list)에 추가합니다.
        sums_list.append(current_sum)
        
    # 9. 모든 구간 합이 저장된 리스트에서 최댓값(max_sum)과
    #    최솟값(min_sum)을 찾습니다.
    max_sum = max(sums_list)
    min_sum = min(sums_list)
    
    # 10. 문제의 요구사항인 (최댓값 - 최솟값)을 계산합니다.
    result = max_sum - min_sum
        
    # 11. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")