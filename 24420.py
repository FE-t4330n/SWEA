# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for _ in range(T):
    
    # 2. N, M (집합 A, B의 크기) - 이 문제에서는 굳이 쓸 필요 없습니다.
    input() 
    
    # 3. A와 B의 원소를 입력받아 set으로 만듭니다.
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))
    
    result = ""
    
    # 4. 규칙에 따라 관계를 확인합니다.
    if set_A == set_B:
        result = "="
    elif set_A < set_B:  # A가 B의 진부분집합인가?
        result = "<"
    elif set_A > set_B:  # A가 B의 진초집합인가?
        result = ">"
    else:
        result = "?"
        
    # 5. 결과를 출력합니다. (이 문제는 #tc 번호가 없는 형식입니다)
    print(result)