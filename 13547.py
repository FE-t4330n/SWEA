# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

# 2. 각 테스트 케이스(1부터 T까지)에 대해 반복합니다.
for test_case in range(1, T + 1):
    
    # 3. 현재까지의 경기 결과 문자열 S를 입력받습니다.
    S = input()
    
    # 4. 총 경기 횟수는 15회로 고정되어 있습니다.
    total_games = 15
    
    # 5. 소정이가 승리해야 하는 횟수(과반수)는 8회입니다.
    wins_needed = 8
    
    # 6. 현재까지 소정이가 승리한 횟수(current_wins)를 셉니다.
    #    (문자열 S에서 'o'의 개수를 셉니다)
    current_wins = S.count('o')
    
    # 7. 현재까지 진행한 경기 수(games_played)를 셉니다.
    #    (문자열 S의 길이입니다)
    games_played = len(S)
    
    # 8. 남은 경기 수(remaining_games)를 계산합니다.
    remaining_games = total_games - games_played
    
    # 9. 소정이가 남은 경기를 모두 이겼을 때의
    #    최대 승리 횟수(max_possible_wins)를 계산합니다.
    max_possible_wins = current_wins + remaining_games
    
    # 10. 최종 결과를 저장할 변수(result)를 기본값 "NO"로 설정합니다.
    result = "NO"
    
    # 11. 만약 최대 가능 승리 횟수(max_possible_wins)가
    #     승리 조건(wins_needed, 8)보다 크거나 같다면,
    if max_possible_wins >= wins_needed:
        
        # 12. 아직 우승 가능성이 있으므로, 결과를 "YES"로 변경합니다.
        result = "YES"
        
    # 13. 형식에 맞춰 테스트 케이스 번호와 결과(result)를 출력합니다.
    print(f"#{test_case} {result}")