# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(컨테이너 수), M(트럭 수)
    N, M = map(int, input().split())
    
    # 4. 컨테이너 무게, 트럭 용량 입력
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    
    # 5. 둘 다 내림차순 정렬
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    
    # 7. 총 무게, 인덱스 초기화
    total_weight = 0
    c_idx = 0  # 컨테이너 포인터
    t_idx = 0  # 트럭 포인터
    
    # 9. 트럭과 컨테이너가 모두 남아있는 동안 반복
    while t_idx < M and c_idx < N:
        
        # 10. (경우 1) 트럭이 컨테이너를 실을 수 있는 경우
        if trucks[t_idx] >= containers[c_idx]:
            total_weight += containers[c_idx]
            t_idx += 1  # 이 트럭은 사용함
            c_idx += 1  # 이 컨테이너는 실었음
        else:
        # 11. (경우 2) 가장 큰 트럭이 이 컨테이너를 못 실음
        #        -> 이 컨테이너는 아무도 못 실음
            c_idx += 1  # 이 컨테이너는 포기
            
    # 12. 결과 출력
    print(f"#{test_case} {total_weight}")