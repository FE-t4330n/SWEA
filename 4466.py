# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. N(총 과목 수), K(선택할 과목 수)를 입력받습니다.
    N, K = map(int, input().split())
    
    # 4. N개의 과목 점수를 리스트로 입력받습니다.
    scores = list(map(int, input().split()))
    
    # 5. 점수를 '내림차순'(높은 점수부터)으로 정렬합니다.
    scores.sort(reverse=True)
    
    # 6. 정렬된 리스트의 앞에서 K개(가장 높은 K개)의 총합을 구합니다.
    #    sum()과 리스트 슬라이싱(scores[0:K])을 사용합니다.
    max_total = sum(scores[0:K])
    
    # 7. 형식에 맞춰 출력
    print(f"#{test_case} {max_total}")