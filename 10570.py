def is_palindrome(n):
    """ 숫자가 팰린드롬인지 확인하는 함수 """
    s = str(n)
    return s == s[::-1]

# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. A, B를 입력받습니다.
    A, B = map(int, input().split())
    
    # 3. 제곱 팰린드롬의 개수를 셀 변수
    count = 0
    
    # 4. 1부터 (B의 제곱근)까지만 반복
    #    B의 최대값은 1000, sqrt(1000)은 약 31.6이므로 32까지만 확인
    i = 1
    while True:
        # 5. 제곱근의 제곱(N)을 계산
        N = i * i
        
        # 6. N이 B보다 커지면 더 이상 볼 필요가 없음
        if N > B:
            break
            
        # 7. N이 A보다 크거나 같아야 범위에 포함됨
        if N >= A:
            # 8. 조건 1: 제곱근(i)이 팰린드롬인가?
            # 9. 조건 2: 제곱수(N)가 팰린드롬인가?
            if is_palindrome(i) and is_palindrome(N):
                count += 1
                
        # 다음 숫자로
        i += 1
        
    # 10. 형식에 맞춰 출력
    print(f"#{test_case} {count}")