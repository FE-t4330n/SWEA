# 총 10개의 테스트 케이스 고정
for test_case in range(1, 11):
    
    # 2. 찾아야 할 회문의 길이 M
    M = int(input())
    
    # 3. 8x8 격자판 입력
    board = [input() for _ in range(8)]
    
    # 4. 회문 개수 카운트
    count = 0
    
    # 5. 가로 탐색
    for i in range(8):
        # j는 0부터 (8-M)까지만 순회하면 됨
        for j in range(8 - M + 1):
            # 가로로 M글자 자르기
            word = board[i][j : j + M]
            
            # 팰린드롬 검사
            if word == word[::-1]:
                count += 1

    # 6. 세로 탐색
    # (M == 8일 때도 range(1)이 되어야 하므로 8-M+1)
    for i in range(8 - M + 1): 
        for j in range(8):
            # 세로로 M글자 만들기
            word_vertical = ""
            for k in range(M):
                word_vertical += board[i+k][j]

            # 팰린드롬 검사
            if word_vertical == word_vertical[::-1]:
                count += 1
                
    # 7. 결과 출력
    print(f"#{test_case} {count}")