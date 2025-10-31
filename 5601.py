# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 사람의 수 N을 입력받습니다.
    N = int(input())
    
    # 3. 각자 마실 양 "1/N"을 저장할 리스트
    results = []
    
    # 4. N명 모두 1/N 씩 마시게 됩니다.
    for _ in range(N):
        # 5. "p/q" 형식의 문자열로 만듭니다.
        results.append(f"1/{N}")
        
    # 6. 형식에 맞춰 출력 (*results는 리스트를 공백으로 구분하여 출력)
    print(f"#{test_case}", *results)