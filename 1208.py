# 1. 이 문제는 테스트 케이스가 10개로 고정되어 있습니다.
#    (따라서 T를 입력받지 않고 1부터 10까지 반복합니다)
for test_case in range(1, 11):
    
    # 2. 덤프를 수행할 수 있는 횟수(dump_count)를 정수로 입력받습니다.
    dump_count = int(input())
    
    # 3. 100개의 상자 높이(boxes)를 리스트로 입력받습니다.
    boxes = list(map(int, input().split()))
    
    # 4. 주어진 덤프 횟수(dump_count)만큼 반복합니다.
    for _ in range(dump_count):
        
        # 5. [핵심] 매번 덤프 전에 리스트를 오름차순으로 정렬합니다.
        boxes.sort()
        
        # 6. 정렬 후, 가장 낮은 값(min_val)과 가장 높은 값(max_val)을 찾습니다.
        min_val = boxes[0]    # 맨 앞
        max_val = boxes[99]   # 맨 뒤 (인덱스 -1과 동일)
        
        # 7. [종료 조건] 현재 높이 차가 1 이하(0 또는 1)이면,
        #     더 이상 평탄화할 수 없으므로 덤프 작업을 중단합니다.
        if (max_val - min_val) <= 1:
            break
            
        # 8. 덤프 수행:
        #    가장 높은 곳(99번 인덱스)은 1 감소시키고,
        #    가장 낮은 곳(0번 인덱스)은 1 증가시킵니다.
        boxes[99] -= 1
        boxes[0] += 1
        
    # 9. 모든 덤프 작업이 끝난 후,
    #    *최종* 상태의 리스트를 다시 한번 정렬하여
    #    최종 최댓값과 최솟값을 확인합니다.
    #    (마지막 덤프로 순서가 바뀌었을 수 있으므로 필수)
    boxes.sort()
    
    # 10. 최종적인 높이 차(result_diff)를 계산합니다.
    result_diff = boxes[99] - boxes[0]
            
    # 11. 형식에 맞춰 테스트 케이스 번호와 최종 높이 차(result_diff)를 출력합니다.
    print(f"#{test_case} {result_diff}")