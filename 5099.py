# 0. 큐(Queue) 자료구조를 사용하기 위해 deque를 가져옵니다.
from collections import deque

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. N (화덕 크기)과 M (피자 개수)을 정수로 입력받습니다.
    N, M = map(int, input().split())
    
    # 4. M개의 피자에 뿌려진 치즈의 양(C)을 리스트로 입력받습니다.
    C = list(map(int, input().split()))
    
    # 5. 화덕(stove_q)을 큐(deque)로 생성합니다.
    stove_q = deque()
    
    # 6. [초기 단계] 화덕에 처음 N개의 피자를 넣습니다.
    #    (1-based 피자 번호, 치즈 양) 튜플로 저장합니다.
    for i in range(N):
        # (피자 번호 i+1, i번째 피자의 치즈 C[i])
        stove_q.append((i + 1, C[i]))
        
    # 7. 화덕에 다음에 들어갈 피자의 0-based 인덱스(next_pizza_idx)를
    #    N으로 설정합니다. (0~N-1번은 이미 화덕에 있으므로)
    next_pizza_idx = N
    
    # 8. 화덕에 피자가 1개만 남을 때까지(len(stove_q) > 1) 반복합니다.
    while len(stove_q) > 1:
        
        # 9. 큐의 맨 앞에서 피자를 꺼냅니다.
        current_idx, current_cheese = stove_q.popleft()
        
        # 10. 치즈를 반으로 줄입니다 (C // 2).
        current_cheese //= 2
        
        # 11. [조건 1] 치즈가 0보다 큰 경우 (아직 덜 녹음)
        if current_cheese > 0:
            # 12. 큐의 맨 뒤에 다시 집어넣습니다.
            stove_q.append((current_idx, current_cheese))
            
        # 13. [조건 2] 치즈가 0이 된 경우 (다 녹음)
        else:
            # 14. 아직 화덕에 못 들어간 대기 피자가(next_pizza_idx < M) 있는지 확인합니다.
            if next_pizza_idx < M:
                
                # 15. 대기 중인 다음 피자를 화덕에 넣습니다.
                #     (피자 번호 next_pizza_idx + 1, 치즈 C[next_pizza_idx])
                stove_q.append((next_pizza_idx + 1, C[next_pizza_idx]))
                
                # 16. 다음 대기 피자 인덱스를 1 증가시킵니다.
                next_pizza_idx += 1
                
            # 17. (만약 대기 피자가 없다면? -> 아무것도 넣지 않고 큐의 크기가 1 줄어듭니다)
            
    # 18. while 루프가 끝나면 큐에는 1개의 피자만 남습니다.
    #     그 피자를 꺼내 번호(final_pizza_idx)를 확인합니다.
    final_pizza_idx, _ = stove_q.popleft()
            
    # 19. 형식에 맞춰 테스트 케이스 번호와 최종 피자 번호를 출력합니다.
    print(f"#{test_case} {final_pizza_idx}")