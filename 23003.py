# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 색상 휠의 순서를 리스트로 정의합니다.
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    # 4. 두 색상 S와 T를 공백으로 구분하여 입력받습니다.
    S, T = input().split()
    
    # 5. 결과를 저장할 변수(result)를 선언합니다.
    result = ""
    
    # 6. [조건 1] 두 색상이 같은지 확인합니다. ('E')
    if S == T:
        result = "E"
    
    # 7. 두 색상이 다른 경우, 나머지 관계를 판별합니다.
    else:
        # 8. 리스트에서 두 색상의 인덱스(위치)를 찾습니다.
        s_idx = colors.index(S)
        t_idx = colors.index(T)
        
        # 9. 두 인덱스 차이의 절댓값을 계산합니다.
        diff = abs(s_idx - t_idx)
        
        # 10. 휠은 원형이므로, 최단 거리를 계산합니다.
        #     (예: 0번 "red"와 5번 "purple"의 차이는 5지만,
        #      반대쪽 최단 거리는 6-5 = 1 입니다.)
        shortest_dist = min(diff, 6 - diff)
        
        # 11. [조건 2] 최단 거리가 1이면 '인접'입니다. ('A')
        if shortest_dist == 1:
            result = "A"
            
        # 12. [조건 3] 최단 거리가 3이면 '반대편'입니다. ('C')
        elif shortest_dist == 3:
            result = "C"
            
        # 13. [조건 4] 최단 거리가 2이면 '기타'입니다. ('X')
        else:
            result = "X"
            
    # 14. [수정된 부분] 형식에 맞춰 결과(result)만 출력합니다.
    print(f"{result}")