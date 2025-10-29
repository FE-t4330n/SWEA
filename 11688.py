# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. T만큼 반복
for test_case in range(1, T + 1):
    
    # 3. 이동 경로 문자열을 입력받습니다.
    path = input()
    
    # 4. 루트 노드(1/1)로 a, b를 초기화합니다.
    a = 1
    b = 1
    
    # 5. 경로의 각 문자를 순회
    for move in path:
        if move == 'L':
            # 6. 왼쪽 자식 규칙: a / (a+b)
            b = a + b
        elif move == 'R':
            # 7. 오른쪽 자식 규칙: (a+b) / b
            a = a + b
            
    # 8. 최종 a, b를 형식에 맞춰 출력
    print(f"#{test_case} {a} {b}")