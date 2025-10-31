# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. N(총 학생 수), K(제출 학생 수)를 입력받습니다.
    N, K = map(int, input().split())
    
    # 3. 1부터 N까지의 '전체 학생' set을 만듭니다.
    all_students = set(range(1, N + 1))
    
    # 4. '제출한 학생' set을 만듭니다.
    submitted_students = set(map(int, input().split()))
    
    # 5. 차집합 연산(-)으로 제출하지 않은 학생을 찾습니다.
    not_submitted = all_students - submitted_students
    
    # 6. set을 리스트로 변환하고 오름차순으로 정렬합니다.
    result_list = sorted(list(not_submitted))
    
    # 7. 형식에 맞춰 출력 (리스트 앞에 *를 붙이면 공백으로 구분되어 출력됨)
    print(f"#{test_case}", *result_list)