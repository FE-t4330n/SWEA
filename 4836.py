# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 빨간색(1)과 파란색(2)이 칠해진 좌표를 저장할 set
    set_r = set()
    set_b = set()
    
    # 3. 칠할 영역의 수 N
    N = int(input())
    
    # 4. N개의 영역을 순서대로 칠합니다.
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 5. 사각형의 모든 칸(r, c)을 순회
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                
                # 6. 좌표 (r, c)를 튜플로 만들어
                #    알맞은 set에 추가 (set은 중복을 자동 제거)
                if color == 1:
                    set_r.add((r, c))
                else: # color == 2
                    set_b.add((r, c))

    # 7. 'set_r'와 'set_b'의 교집합(intersection)을 구합니다.
    #    '&' 연산자는 교집합을 의미합니다.
    purple_cells = set_r & set_b
    
    # 8. 교집합의 크기(원소의 개수)가 보라색 칸의 수입니다.
    purple_count = len(purple_cells)
                
    print(f"#{test_case} {purple_count}")